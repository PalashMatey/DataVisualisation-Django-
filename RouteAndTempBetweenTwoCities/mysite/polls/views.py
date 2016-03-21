from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Temperature
from django.template import loader
from django.http import Http404
import pyowm
owm = pyowm.OWM('29d7de7caa102eec0f97034cd9f208cb')
#latest_temperature_list = []
def index(request):
     #global latest_temperature_list
     ##latest_temperature_list = Temperature.objects.order_by('-timestamp')[:5]
     city_list = Question.objects.order_by('-city_text')[:5]
     template = loader.get_template('polls/index.html')
     context = {
		#'latest_question_list' : latest_question_list,

		'city_list' : city_list,
	}
     #output = ', '.join([q.question_text for q in latest_question_list])
     #return HttpResponse(template.render(context,request))
     return render(request,'polls/index.html',context)
#     return HttpResponse(output)
#    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def detail(request, city_id):
    try:
	city = Question.objects.get(pk=city_id)
	observation = owm.weather_at_place(city.city_text+',US')
	w = observation.get_weather()
	x =  w.get_temperature('celsius')
	city.temp = x['temp']
	#question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
	raise Http404("Question does not exist")

    return render(request,'polls/detail.html',{'city': city})

def route(request):
    city_start = Question.objects.get(city_text=(request.POST['group1']))
    #city_list = []
    #city_list.append(request.POST['group1'])
    #city_list.append(request.POST['group2'])
    #city_list2 = []
    city_end = Question.objects.get(city_text=(request.POST['group2']))
    city1 = request.POST['group1']
    city2 = request.POST['group2']
    observation1 = owm.weather_at_place(city1+',US')
    w1 = observation1.get_weather()
    x1 =  w1.get_temperature('celsius')
    #city_list2.append(x1['temp'])
    city_start.temp = x1['temp']
    observation2 = owm.weather_at_place(city2+',US')
    w2 = observation2.get_weather()
    x2 =  w2.get_temperature('celsius')
    #city_list2.append(x2['temp'])
    city_end.temp = x2['temp']
    #mylist = zip(city_list, city_list2)i
    return  render(request,'polls/route.html', {'city_start' : city_start, 'city_end' : city_end})       


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

