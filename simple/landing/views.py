from django.shortcuts import render
from django.http import HttpResponse


def get_main(request):
    return HttpResponse("<h1> Success </h1>")


def get_elements(request):
    return render(request, 'elements.html', {})


def get_generic(request):
    return render(request, 'generic.html', {})


def get_index(request):
    return render(request, 'index.html', {})
