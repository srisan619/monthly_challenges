from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = ''
    if month=="january":
        challenge_text="Go to Yoga practice for every week"
    elif month=="february":
        challenge_text="Go to walk on daily basis"
    elif month=="march":
        challenge_text="Study books learning month"
    elif month=="april":
        challenge_text="Travel somewhere in the world"
    elif month=="may":
        challenge_text="Start learning cooking on may month"
    elif month=="june":
        challenge_text="Birthday months, lets celebrate!"
    else:
        return HttpResponseNotFound("This is not month, Please check and try the correct month")
        
    return HttpResponse(challenge_text)