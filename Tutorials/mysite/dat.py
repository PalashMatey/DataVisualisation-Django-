import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from datetime import datetime
from polls.models import Question, Temperature
#from django.utils import timezone
import pyowm
import geopy
from geopy.geocoders import Nominatim

cities = ['New York','San Francisco','Boston','Chicago']
owm = pyowm.OWM('29d7de7caa102eec0f97034cd9f208cb')
print Question.objects.all()
#print Temperature.objects.all()
#for i in range(0,4):
	
#	q = Question(city_text=cities[i])
#	q.save()

#print Question.objects.all()
for i in range(0,4):
	
	q = Question.objects.filter(city_text=cities[i])
			
	#print q.temperature_set.all()
	observation = owm.weather_at_place(str(cities[i])+',US')
	w = observation.get_weather()
	x = w.get_temperature('celsius')		
	geolocator = Nominatim()
	y = geolocator.geocode(cities[i])
	t = []
	fin = y.raw
	lo = fin['lon']
	la = fin['lat']
	q.update(lat = la,lon = lo)
	#print q.lon
	#print q.lat
	#q.temperature_set.create(temperature_data= x['temp'])
	#t.temperature_set.create(location = c)
	#print q.temperature_set.all()
	#print t.temperature_set.all()
