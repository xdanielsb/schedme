from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Students")


def landing(request):
    context = {}
    return render(request, "students/landing.html", context)
