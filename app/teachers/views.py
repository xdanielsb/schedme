# Create your views here.
from django.http import JsonResponse
from common.timetable_functions import generate_random_teachers
from teachers.models import Teacher, Class
from django.shortcuts import render, redirect


def index(request):
    context = {}
    teachers = Teacher.objects.all()
    context["teachers"] = teachers
    return render(request, "teachers/index.html", context)


def desc(request, id):
    context = {}
    teacher = Teacher.objects.get(pk=id)
    classes = Class.objects.filter(teacher=teacher)
    # hobbies = ", ".join([h.name for h in hobbies_user])
    context["teacher"] = teacher
    context["classes"] = classes
    return render(request, "teachers/calendart.html", context)


def generate_test_teachers(request):
    return JsonResponse({"teachers": generate_random_teachers(10)}, status=200)
