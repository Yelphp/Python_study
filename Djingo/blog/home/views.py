from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 你的第一个应用")