from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse

from django.template.context_processors import csrf
from refinator.forms.users import NewUserForm

# http://code.techandstartup.com/django/registration/


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/complete')

    else:
        form = NewUserForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.djhtml', token)


def registration_complete(request):
    messages.add_message(request, messages.SUCCESS,
                         "You can login now with your credentials.")
    return redirect(reverse('refinator:login'))
