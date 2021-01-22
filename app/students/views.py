import datetime
from django.shortcuts import render, redirect
from teachers.models import Teacher, Class
from students.models import Hobbie, FreeTime, CalendarCredentials, Activity
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from common.calendar import get_events, filter_creds
import pickle
from common.timetable_functions import generate_random_teachers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import random


def landing(request):
    context = {}
    return render(request, "students/landing.html", context)


def index(request):
    context = {}
    hobbies_user = Hobbie.objects.filter(student=request.user)
    free_times = FreeTime.objects.filter(student=request.user)
    activities = Activity.objects.filter(student=request.user)

    hobbies = ", ".join([h.name for h in hobbies_user])
    context["hobbies"] = hobbies
    context["free_times"] = free_times
    context["activities"] = activities
    return render(request, "students/calendar.html", context)


def guest(request):
    context = {}
    name = "guest{}".format(random.randint(1, 1000))
    if len(User.objects.filter(username=name)) == 0:
        user = User.objects.create_user(
            username=name,
            password="some-secret-password",
            first_name=name,
            last_name=" H.",
        )
        user.save()
    user = authenticate(username=name, password="some-secret-password")
    login(request, user)
    return render(request, "students/calendar.html", context)


def save_hobbies(request):
    hobbies = request.POST.get("hobbies")
    Hobbie.objects.filter(student=request.user).delete()
    for _hobbie in [x.strip().lower() for x in hobbies.split(",")]:
        hob = Hobbie(student=request.user, name=_hobbie)
        hob.save()
    return redirect("students:index")


def load_calendar(request):
    # here call method load calendar
    # print(request.user)  # current user
    # obtain calendar token

    creds = CalendarCredentials.objects.filter(student=request.user)
    creds = pickle.loads(creds[0].credentials) if creds else None
    creds = filter_creds(creds)
    CalendarCredentials.objects.update_or_create(
        student=request.user, defaults={"credentials": pickle.dumps(creds)}
    )
    # obtain google calendar data and store it in our database
    events = get_events(creds)
    for event in events:
        default_value = {
            "start": event["start"]["dateTime"],
            "end": event["end"]["dateTime"],
            "isLocal": False,
        }
        if "title" in event.keys():
            default_value["title"] = event["title"]
        Activity.objects.update_or_create(
            student=request.user, google_id=event["id"], defaults=default_value
        )
        messages.info(
            request,
            "The events in your calendar was successfully lodaded.",
        )
    return redirect("students:index")


def save_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    start_obj = datetime.datetime.strptime(start, "%m/%d/%Y %H:%M %p")
    end_obj = datetime.datetime.strptime(end, "%m/%d/%Y %H:%M %p")
    obj = FreeTime(student=request.user, start=start_obj, end=end_obj)
    obj.save()
    return JsonResponse({"ok": "true"}, status=200)


def logouts(request):
    logout(request)
    return HttpResponseRedirect("/")


def generate_plan(request):
    context = {}
    # here call method to generate possible plan and
    # generate events to the students
    teachers = Teacher.objects.all()
    if len(teachers) <= 5:
        for row in generate_random_teachers(10):
            t = Teacher(
                name=row["name"], email=row["email"], last_name=row["last_name"]
            )
            t.save()
            for p in row["proposals"]:
                nclass = Class(
                    teacher=t,
                    topic=p["topic"],
                    start=p["start"],
                    end=p["end"],
                    slots=p["number_of_slots"],
                )
                nclass.save()

    free_times = FreeTime.objects.filter(student=request.user)
    activities = Activity.objects.filter(student=request.user)

    possible_classe = []
    for free_time in free_times:
        for activity in activities:
            # available classes at that time with that topic for that user
            ans = Class.objects.filter(
                start__gte=free_time.start, end__leq=free_time.end
            )
            if len(ans) > 0:
                possible_classe.append(ans[0])
                break

    if len(possible_classe) == 0:
        messages.info(
            request,
            "There are not available classes that match your free times & hobbies, go to Teachers, we propose you some random classes",
        )
        possible_classe = random.sample(list(Class.objects.all()), 3)
    context["classes"] = possible_classe

    hobbies_user = Hobbie.objects.filter(student=request.user)
    hobbies = ", ".join([h.name for h in hobbies_user])
    context["hobbies"] = hobbies
    context["free_times"] = free_times
    context["activities"] = activities

    return render(request, "students/calendar.html", context)
