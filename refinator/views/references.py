from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from refinator.models import Reference, Comment


def ref_index(request):
    ref_list = Reference.objects.order_by("ref_name")
    context = {'ref_list': ref_list}
    return render(request, 'refinator/index.html', context)

def ref_detail(request, ref_id):
    ref = get_object_or_404(Reference, pk=ref_id)
    return render(request, 'refinator/detail.html', {'ref': ref})

def ref_vote(request, ref_id, vote_type):
    ref = get_object_or_404(Reference, pk=ref_id)
    if vote_type == "up":
        ref.votes += 1
    else:
        ref.votes -= 1
    ref.save()
    return HttpResponseRedirect(reverse('refinator:detail', args=(ref.id,)))
