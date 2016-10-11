from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from refinator.models import Reference, Comment, ReferenceVote, ReferenceForm


def ref_index(request, page_no):
    ref_list = Reference.objects.order_by("ref_name")
    paginator = Paginator(ref_list, 10)

    try:
        refs = paginator.page(page_no)
    except PageNotAnInteger:
        refs = paginator.page(1)
    except EmptyPage:
        regs = paginator.page(paginator.num_pages)

    context = {'ref_list': refs, 'first_time': False}

    if not request.session.has_key('first_time'):
        context['first_time'] = True
        request.session['first_time'] = False


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


def ref_edit(request, ref_id=None):
    if request.user.is_authenticated:
        if ref_id:
            # editing
            ref = get_object_or_404(Reference, id=ref_id)
            edit = True
        else:
            ref = Reference(added_by=request.user)
            edit = False

        if request.method == "POST":
            form = ReferenceForm(request.POST, instance=ref)
            if form.is_valid():
                ref = form.save(commit=False)
                ref.added_by = request.user
                ref.save()
                vote = ReferenceVote(user=request.user, ref=ref, vote_amount=1)
                vote.save()
                form.save_m2m()
                messages.add_message(request, messages.SUCCESS,
                                     "Thanks for your contribution!")
                return redirect(
                    'refinator:ref_detail', ref_id=ref.id)
        else:
            form = ReferenceForm(instance=ref)
        return render(request, 'refs/ref-new.html', {'edit': edit, 'form': form})
    else:
        messages.add_message(request, messages.ERROR, mark_safe(
                             'You must log in to add or edit references. ' \
                             '(Maybe you\'d like to <a href="/register/" class="alert-link">sign up</a> instead?)'))
        return redirect('refinator:login')
