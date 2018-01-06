from django.db import models
from bs4 import BeautifulSoup
import requests


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class AnanLib(models.Model):
    # uri = 'http://faketurn.com/rs/'
    # r = requests.get(uri)
    # soup = BeautifulSoup(r.content, 'html.parser')
    text = '1246'
