from django.shortcuts import render, HttpResponse
from django import template
import requests
import json


def get_function():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.request("GET", url).json()
    return response


def index(request):
    response_api = get_function()
    data = {'astronauts': response_api}
    return render(request, 'core/index.html', data)


# json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
# json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
