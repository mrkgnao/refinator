from django.shortcuts import render, redirect


def about(request):
    return render(request, 'main/about.djhtml')


def contact(request):
    return render(request, 'main/contact.djhtml')
