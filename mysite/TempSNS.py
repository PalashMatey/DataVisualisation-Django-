import boto3
import mraa
import time
import thread
from math import log
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from polls.models import Temp

# Boto3 Init
#client = boto3.client('sns', 'us-east-1')

#topic_arn='arn:aws:sns:us-east-1:602386368437:Lab4Q1'
#message_subject='CurrentTemp'
#account_ID=['602386368437']
#action_name=['AddPermission']

#client.add_permission(TopicArn=topic_arn, Label='Temp SNS', AWSAccountId=account_ID, ActionName=action_name)

# Temperature Sensor Init
tempPin = 1
tempSensor = mraa.Aio(tempPin)

def TempRead(e):

	global tempSensor
	
	# Define constants
        B = 4275
        R0 = 100000.0

	while True:

	        # Get raw value
        	raw = tempSensor.read()

        	# Calculate
        	R = 1023.0/raw - 1.0
        	R = R0*R
        	temp1 = 1.0/(log(R/R0)/B+1/298.15)-273.15
		temp1 = int(temp1)
		t = Temp(temp = temp1)
		t.save()		
		time.sleep(3)

try:
   thread.start_new_thread( TempRead , ("Thread-1", ) )
except:
   print "Error: unable to start thread"

while True:
	pass

