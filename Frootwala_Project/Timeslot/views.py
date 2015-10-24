from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from Timeslot.models import Slots
from Timeslot.serializers import TimeSlotSerializer
import datetime


class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse,self).__init__(content,**kwargs)

def slot_list(request,day_type):
	if day_type == "Tomorrow":
		queryset = Slots.objects.filter(day=day_type)
		
	elif day_type =="Today":
		queryset = Slots.objects.filter(day=day_type)
		if datetime.datetime.now.hour > 20:
			queryset = queryset.filter(id__gt = 3)
		elif datetime.datetime.now.hour > 17:
			queryset = queryset.filter(id__gt = 2)
		elif datetime.datetime.now.hour > 13:
			queryset = queryset.filter(id__gt = 1)

	serializer = TimeSlotSerializer(queryset,many=True)
	return JSONResponse(serializer.data)

def alt_slot_list(request):
	queryset = Slots.objects.all()

	if datetime.datetime.now.hour > 20:
		queryset = queryset.filter(id__gt = 3)
	elif datetime.datetime.now.hour > 17:
		queryset = queryset.filter(id__gt = 2)
	elif datetime.datetime.now.hour > 13:
		queryset = queryset.filter(id__gt = 1)

	serializer = TimeSlotSerializer(queryset,many=True)
	return JSONResponse(serializer.data)
