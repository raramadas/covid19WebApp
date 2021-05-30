import requests
from django.shortcuts import render
from django.http import HttpResponse


def dailyCount(request):
    try:
        if request.method == 'GET':
            response = requests.get('https://api.covid19india.org/v4/min/data.min.json')
            data = response.json()
            return HttpResponse(data)
    except Exception:
        return ("Invalid Request")
