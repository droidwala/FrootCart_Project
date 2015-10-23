from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Offers.models import Offers
from Offers.serializers import OfferSerializer

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse,self).__init__(content,**kwargs)

def offers_list(request):
	offers = Offers.objects.all()
	serializer = OfferSerializer(offers,many=True)
	return JSONResponse(serializer.data)





	


# Create your views here.
