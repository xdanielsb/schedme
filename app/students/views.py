from django.shortcuts import render, redirect
from students.models import Student
from teachers.models import Teacher


def landing(request):
    context = {}
    return render(request, "students/landing.html", context)


def index(request):
    context = {}
    return render(request, "students/calendar.html", context)


def save_hobbies(request):
    hobbies = request.POST.get("hobbies")
    print(hobbies)
    return redirect('students:index')


def load_calendar(request):
    context = {}
    # here call method load calendar
    print(request.user)  # current user
    return render(request, "students/calendar.html", context)


def generate_plan(request):
    context = {}
    # here call method to generate possible plan and
    # generate events to the students
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    # current students and teachers
    print(students)
    print(teachers)
    # call function to generate schedules
    return render(request, "students/calendar.html", context)
