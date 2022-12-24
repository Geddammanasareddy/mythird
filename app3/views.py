from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project(request):
    return HttpResponse('<i>my first project is python</i>')

def one(request):
    return HttpResponse('<marquee><h1> python full stack</h1></marquee')
