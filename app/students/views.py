from django.shortcuts import render


def landing(request):
    context = {}
    return render(request, "students/landing.html", context)


def index(request):
    context = {}
    return render(request, "students/calendar.html", context)
