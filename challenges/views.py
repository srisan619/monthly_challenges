from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html")
        # response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
    
def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path =  reverse("month-challenge", args=[redirect_month])
    print(redirect_month)
    return HttpResponseRedirect(redirect_path)
    