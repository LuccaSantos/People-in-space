from django.shortcuts import render, HttpResponse
import requests
import json


# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     return(text)

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
