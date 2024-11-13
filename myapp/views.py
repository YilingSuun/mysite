from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu
# Create your views here


def index(request):
    return HttpResponse("Hello world!")


def add(request):
    my_str = ''
    lists = Stu.objects.all()
    for stu in lists:
        my_str = my_str + str(stu) + '\n'

    # print(Stu.objects.get(id=3))
    return HttpResponse("Add..........." + my_str)

