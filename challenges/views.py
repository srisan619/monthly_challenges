from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("Go to Yoga practice for every week")

def february(request):
    return HttpResponse("Go to walk on daily basis")