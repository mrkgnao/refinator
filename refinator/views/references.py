from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from refinator.models import Reference, Comment, ReferenceVote, ReferenceForm

def ref_index(request):
    ref_list = Reference.objects.order_by("ref_name")
    context = {'ref_list': ref_list}
    if request.user:
        context['user'] = request.user
    return render(request, 'refs/ref-index.html', context)

def ref_detail(request, ref_id):
    ref = get_object_or_404(Reference, pk=ref_id)
    has_upvoted = ReferenceVote.user_has_upvoted(request.user, ref)
    has_downvoted = ReferenceVote.user_has_downvoted(request.user, ref)
    return render(request, 'refs/ref-detail.html', {
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

def ref_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReferenceForm(request.POST)
            if form.is_valid():
                ref = form.save(commit=False)
                ref.added_by = request.user
                ref.save()
                form.save_m2m()
                return redirect('refinator:ref_detail', ref_id=ref.id)
        else:
            form = ReferenceForm()
        return render(request, 'refs/ref-new.html', {'form': form})
    else:
        messages.add_message(request, messages.ERROR, 'You must log in to add new references.')
        return redirect('refinator:login')
