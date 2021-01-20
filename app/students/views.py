import datetime
from django.shortcuts import render, redirect
from teachers.models import Teacher
from students.models import Hobbie, FreeTime
from django.contrib.auth.models import User
from django.http import JsonResponse


def landing(request):
    context = {}
    return render(request, "students/landing.html", context)


def index(request):
    context = {}
    hobbies_user = Hobbie.objects.filter(student=request.user)
    hobbies = ", ".join([h.name for h in hobbies_user])
    context["hobbies"] = hobbies
    return render(request, "students/calendar.html", context)


def save_hobbies(request):
    hobbies = request.POST.get("hobbies")
    Hobbie.objects.filter(student=request.user).delete()
    for _hobbie in [x.strip().lower() for x in hobbies.split(",")]:
        hob = Hobbie(student=request.user, name=_hobbie)
        hob.save()
    return redirect("students:index")


def load_calendar(request):
    context = {}
    # here call method load calendar
    # print(request.user)  # current user
    return render(request, "students/calendar.html", context)


def save_event(request):
    title = request.GET.get("title", None)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    start_obj = datetime.datetime.strptime(start, '%m/%d/%Y %H:%M %p')
    end_obj = datetime.datetime.strptime(end, '%m/%d/%Y %H:%M %p')
    obj = FreeTime(student=request.user, start=start_obj, end=end_obj)
    obj.save()
    print(title, start, end)  # current user
    return JsonResponse({"ok": "true"}, status=200)


def generate_plan(request):
    context = {}
    # here call method to generate possible plan and
    # generate events to the students
    students = User.objects.all()
    teachers = Teacher.objects.all()
    # current students and teachers
    # print(students)
    # print(teachers)
    # call function to generate schedules
    return render(request, "students/calendar.html", context)
