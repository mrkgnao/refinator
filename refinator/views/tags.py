from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from refinator.models import Reference, Comment, Tag

def tag_index(request, page_no):
    tag_list = Tag.objects.order_by("tag_name")
    paginator = Paginator(tag_list, 10)

    try:
        tags = paginator.page(page_no)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        regs = paginator.page(paginator.num_pages)

    context = {'tag_list': tags}
    return render(request, 'tags/tag-index.html', context)

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'tags/tag-detail.html', {'tag': tag})
