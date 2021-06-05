import requests
from django.shortcuts import render
from django.http import HttpResponse

def dailyApiCall(request):
    try:
        if request.method == "GET":
            url = "https://api.covid19india.org/v4/min/data.min.json"
            response = requests.get(url)
            data = response.json()
            return HttpResponse(render(request, "index.html",{"data" : data}))
    except Exception:
        return ("Invalid Request")


