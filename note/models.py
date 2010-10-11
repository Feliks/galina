from django.db import models

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
