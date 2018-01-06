from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
# from .models import AnanLib

from bs4 import BeautifulSoup
import requests
# import os


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


# def index(request):
#     r = requests.get('http://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')


# def index(request):
#     times = int(os.environ.get('TIMES', 3))
#     return HttpResponse('Hello! ' * times)


def anan(request):
    uri = 'http://faketurn.com/rs/'
    r = requests.get(uri)
    soup = BeautifulSoup(r.content, 'html.parser')
    texts = soup.title.string
    print(texts)
    return render(request, 'anan.html', {'texts': texts})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

