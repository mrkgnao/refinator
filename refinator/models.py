from django.db import models

class RefTag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

class Reference(models.Model):
    ref_name = models.CharField(max_length=200)
    url      = models.CharField(max_length=200)
    filetype = models.CharField(max_length=20)
    size     = models.IntegerField(default=0)
    author   = models.CharField(max_length=20)
    votes    = models.IntegerField(default=1)

    def __str__(self):
        return "\"{}\" by {}".format(self.ref_name, self.author)

class Comment(models.Model):
    comment_text = models.CharField(max_length=5000)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text
