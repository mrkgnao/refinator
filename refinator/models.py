from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import re
import requests


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_slug = models.CharField(max_length=100)

    desc = models.TextField()

    added_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, default=1)

    def set_slug(self):
        self.tag_slug = re.sub(r"\s+", '-', self.tag_name).lower()

    def save(self, *args, **kwargs):
        self.set_slug()
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        self.set_slug()
        return self.tag_slug

    class Meta:
        ordering = ("tag_slug", )


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            'tag_name',
            'desc',
        ]

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        nicenames = {
            'tag_name': 'Tag name',
            'desc': 'Description',
        }

        placeholders = {
            'tag_name': 'The title of the tag',
            'desc': 'A few words about the topic',
        }

        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({'class': 'form-control', })

        for k in placeholders.keys():
            self.fields[k].widget.attrs.update({
                'placeholder': placeholders[k],
            })

        for k in nicenames.keys():
            self.fields[k].label = nicenames[k]


class Reference(models.Model):
    ref_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    filetype = models.CharField(max_length=20)
    size = models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)

    added_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, default=1)

    desc = models.TextField(default="")

    prereqs = models.ManyToManyField(
        "self", related_name="prereq_for", symmetrical=False, blank=True)
    read_with = models.ManyToManyField(
        "self", related_name="read_with_for", symmetrical=False, blank=True)
    followups = models.ManyToManyField(
        "self", related_name="followup_for", symmetrical=False, blank=True)

    def __str__(self):
        return "{} ({})".format(self.ref_name, self.author)

    def votes_text(self):
        v = self.votes()
        txt = "{} vote".format(v)
        if not (v == 1):
            txt += "s"
        return txt

    def compute_filetype(self):
        self.filetype = self.url.split(".")[-1]

    def get_and_save_size(self):
        try:
            r = requests.head(
                self.url, headers={
                    'Accept-Encoding': 'identity'
                })
            self.size = int(r.headers['content-length'])
        except requests.exceptions.ConnectionError:
            self.size = 0

    def save(self, *args, **kwargs):
        self.compute_filetype()
        self.get_and_save_size()
        super(Reference, self).save(*args, **kwargs)

    def votes(self):
        from functools import reduce
        return reduce(
            lambda x, y: x + y,
            map(lambda v: v.vote_amount,
                ReferenceVote.objects.filter(ref=self)),
            0)


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        fields = [
            'ref_name', 'author', 'desc', 'tags', 'url', 'filetype', 'prereqs',
            'read_with', 'followups'
        ]

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        nicenames = {
            'url': 'URL',
            'ref_name': 'Reference name',
            'desc': 'Description',
        }

        placeholders = {
            'url': 'A link to the file',
            'ref_name': 'The title of the reference',
            'desc': 'A short, helpful description',
            'author': 'John Doe',
            'filetype': 'pdf, djvu, ps, tex, and friends'
        }

        selects = [
            'tags',
            'prereqs',
            'read_with',
            'followups',
        ]

        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({'class': 'form-control', })

        for k in placeholders.keys():
            self.fields[k].widget.attrs.update({
                'placeholder': placeholders[k],
            })

        for s in selects:
            self.fields[s].widget.attrs.update({
                'class': 'form-control show-tick selectpicker',
                'data-live-search': 'false',
            })

        for k in nicenames.keys():
            self.fields[k].label = nicenames[k]


class ReferenceVote(models.Model):
    user = models.ForeignKey(User, default=1)
    ref = models.ForeignKey(Reference)
    vote_amount = models.IntegerField()

    def __str__(self):
        return "{} {} for {}".format(self.user.username, self.vote_amount,
                                     self.ref.ref_name)

    def user_has_voted(user, ref, vote_amount):
        return user.is_authenticated and ReferenceVote.objects.filter(
            user=user, ref=ref, vote_amount=vote_amount).count() > 0

    def user_has_upvoted(user, ref):
        return ReferenceVote.user_has_voted(user, ref, 1)

    def user_has_downvoted(user, ref):
        return ReferenceVote.user_has_voted(user, ref, -1)

    def save(self, *args, **kwargs):
        if ReferenceVote.user_has_voted(self.user, self.ref, self.vote_amount):
            ReferenceVote.objects.filter(user=self.user, ref=self.ref).delete()
        else:
            ReferenceVote.objects.filter(user=self.user, ref=self.ref).delete()
            super(ReferenceVote, self).save(*args, **kwargs)


class Comment(models.Model):
    comment_text = models.TextField()
    speaker = models.ForeignKey(User, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'reference']
