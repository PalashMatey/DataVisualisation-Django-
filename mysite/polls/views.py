from django.shortcuts import render
import json
import time
import mraa
from django.http import HttpResponse
from django.template import loader
from .models import Temp
from math import log
from django.shortcuts import render_to_response

a = ['bazz', 'meg']
'''
def index(request):
    latest_question_list = a
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(a) 
'''
#Temperature Sensor Init

tempPin = 1
tempSensor = mraa.Aio(tempPin)	

def index(request):
	temp = []
	global tempSensor
	f1 = []
	f1.append("Time")
	f1.append("Temperature")
	
	#temp.append(f1)
	latest_temperature_list = Temp.objects.order_by('date')[:10]
	for i in latest_temperature_list.reverse():
		f = []
		#f.append(str(time.time()))
		f.append(str(i.date))
		f.append(i.temp)
		temp.insert(0,f)
		#temp.append(f)
	#temp = temp.reverse()
	temp.insert(0,f1)
	#temp1 = temp1.reverse()
	#temp = temp[:10].reverse()	
	context = {'temp': json.dumps(temp)}
     	return render(request, 'polls/index.html', context)



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# Create your views here.
'''
try:
   thread.start_new_thread( TempRead , ("Thread-1", ) )
except:
   print "Error: unable to start thread"
while True:
	pass
'''
