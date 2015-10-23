from rest_framework import serializers
from Offers.models import Offers

class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offers 
		fields = ('url',)
    #url = serializers.URLField()




