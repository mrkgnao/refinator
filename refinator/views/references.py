from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from refinator.models import Reference, Comment, ReferenceVote


def ref_index(request):
    ref_list = Reference.objects.order_by("ref_name")
    context = {'ref_list': ref_list}
    if request.user:
        context['user'] = request.user
    return render(request, 'refinator/index.html', context)

def ref_detail(request, ref_id):
    ref = get_object_or_404(Reference, pk=ref_id)
    has_upvoted = ReferenceVote.user_has_upvoted(request.user, ref)
    has_downvoted = ReferenceVote.user_has_downvoted(request.user, ref)
    return render(request, 'refinator/detail.html', {
        'ref': ref,
        'has_upvoted': has_upvoted,
        'has_downvoted': has_downvoted,
    })

def ref_vote(request, ref_id, vote_type):
    ref = get_object_or_404(Reference, pk=ref_id)

    if vote_type == "up":
        vote_amount = 1
    else:
        vote_amount = -1

    if request.user.is_authenticated:
        if ReferenceVote.user_has_voted(request.user, ref, vote_amount):
            return HttpResponse(content="ok")
        else:
            if vote_type == "up":
                v = ReferenceVote(ref=ref, user=request.user, vote_amount=1)
            else:
                v = ReferenceVote(ref=ref, user=request.user, vote_amount=-1)
            v.save()
        return HttpResponse(content="ok")
    else:
        return HttpResponseForbidden()
