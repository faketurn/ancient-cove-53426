from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class AnanLib(models.Model):
    # uri = 'http://faketurn.com/rs/'
    # r = requests.get(uri)
    # soup = BeautifulSoup(r.content, 'html.parser')
    # text = soup.title
    text = 'kjdfkj'
