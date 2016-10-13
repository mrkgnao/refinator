from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from refinator.models import Reference, Comment, Tag, TagForm


def search(request, page_no=1, query=""):
    tag_list = Tag.objects.filter(tag_name__icontains=query),
    paginator = Paginator(tag_list, 10)

    try:
        tags = paginator.page(page_no)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        regs = paginator.page(paginator.num_pages)

    context = {'results': tags}

    return render(request, 'tags/search.djhtml', context)


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'tags/tag-detail.djhtml', {'tag': tag})


def tag_edit(request, tag_id=None):
    if request.user.is_authenticated:
        if tag_id:
            # editing
            tag = get_object_or_404(Tag, id=tag_id)
            edit = True
        else:
            tag = Tag(added_by=request.user)
            edit = False

        if request.method == "POST":
            form = TagForm(request.POST, instance=tag)
            if form.is_valid():
                tag = form.save(commit=False)
                tag.added_by = request.user
                tag.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Thanks for your contribution!")
                return redirect('refinator:tag_detail', tag_id=tag.id)
        else:
            form = TagForm(instance=tag)
        return render(request, 'tags/tag-new.djhtml', {
            'edit': edit,
            'form': form
        })
    else:
        messages.add_message(request, messages.ERROR, mark_safe(
                             'You must log in to add or edit tags. ' \
                             '(Maybe you\'d like to <a href="/register/" class="alert-link">sign up</a>?)'))
        return redirect('refinator:login')
