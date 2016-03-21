# DataVisualisation-Django-

Basic Django WebApplication

1) RealTimeTemperatureStreaming
	Application which streams temperature data onto a web page.
	Hardware used is the Intel Edison with a temperature sensor
	

2) RouteAndTempBetweenTwoCities
	Application which has a form that allows you to pick two cities.
	Redirects you to a page which displays the temperature at the two
	cities and also the route information
	
	To run: pip install pyowm
		pip install geopy
		pip install django
	Need the Google developer API key for accessing the google maps api
	
To run either web application:
	python manage.py runserver <your-ip-address>:<port-address>



