from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "Go to Yoga practice for every week",
    "february": "Travel somewhere in the world",
    "march": "Go to Yoga practice for every week",
    "april": "Travel somewhere in the world",
    "may": "Go to Yoga practice for every week",
    "june": "Travel somewhere in the world",
    "july": "Go to Yoga practice for every week",
    "august": "Travel somewhere in the world",
    "september": "Go to Yoga practice for every week",
    "october": "Travel somewhere in the world",
    "november": "Go to Yoga practice for every week",
    "december": "Travel somewhere in the world"
}

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    
def month_challenge_by_number(request, month):
    return HttpResponse(month)
    