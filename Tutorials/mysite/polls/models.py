from __future__ import unicode_literals
from datetime import datetime
from django.db import models
#from django.utils import timezone

# Create your models here.
class Question(models.Model):
	city_text = models.CharField(max_length = 200)
	temp = models.IntegerField(default=0)
	def __str__(self):
		return self.city_text



class Temperature(models.Model):
	temperature = models.ForeignKey(Question,on_delete = models.CASCADE)
	temperature_data = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return str(self.temperature_data)

