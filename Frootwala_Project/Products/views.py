from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from Products.models import Product
from Products.serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse,self).__init__(content,**kwargs)




def products_list(request,types):
	queryset = Product.objects.all()
	#types = self.request.query_params.get('prodtype',None)
	queryset = queryset.filter(prod_type = types) 
	#products = Product.objects.filter(prod_type = type)
	serializer = ProductSerializer(queryset,many=True)
	return JSONResponse(serializer.data)

def search_product(request,prodname):
	queryset = Product.objects.all()
	queryset = queryset.filter(prod_name = prodname)
	serializer = ProductSerializer(queryset,many=True)
	return JSONResponse(serializer.data)




