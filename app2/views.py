from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manasa(request):
    return HttpResponse('<marquee>my project name is project8</marquee>')


def manu(request):
    return HttpResponse('<h1>manu is a good girl</h1>')
