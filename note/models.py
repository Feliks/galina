from django.db import models

#galina
class Events(models.Model):
	event = models.CharField(max_length=500)

class Masters(models.Model):
	master = models.CharField(max_length=30)

class Startstop(models.Model):
	datetimestart = models.TimeField()
	datetimestop = models.TimeField()
	datetimeadd = models.TimeField(auto_now_add=True)
	events = models.ForeignKey(Events)
	masters = models.ForeignKey(Masters)

#books
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
