from rest_framework import serializers
from Timeslot.models import Slots

class TimeSlotSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slots
		fields = ('slot','day',)