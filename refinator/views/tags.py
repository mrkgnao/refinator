from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from refinator.models import Reference, Comment, Tag


def tag_index(request):
    tag_list = Tag.objects.order_by("tag_name")
    context = {'tag_list': tag_list}
    return render(request, 'refinator/tag-index.html', context)

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'refinator/tag-detail.html', {'tag': tag})
