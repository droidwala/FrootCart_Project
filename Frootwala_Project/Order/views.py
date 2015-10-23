from django.http import HttpResponse
from Order.models import order,orderitems
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import simplejson as json
import plivo
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Order.serializers import OrderSerializer

auth_id = "MANGFJOGE4YZDIZJJMYW"
auth_token = "ODY0NTVhYWE0OTFjMDE5YjZjZjU5ODFlOTQ0YWE4"

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse,self).__init__(content,**kwargs)



@csrf_exempt
@transaction.atomic
def post_orders(request):
	if request.method == "POST":
		data = json.loads(request.body)
		order_var = order()
		order_var.user_name = data['name']
		order_var.mobile_num = data['mobile']
		order_var.total_amt = data['total_amt']
		order_var.del_day = data['del_day']
		order_var.del_time = data['del_time']
		order_var.flat_no = data['address']['flat_no']
		order_var.building_name = data['address']['bldg_name']
		order_var.locality_name = data['address']['local_name']
		order_var.city_name = data['address']['city_name']
		order_var.save()
		latest_id = order_var.pk
		
		json_list = data['products']
		for i in range(len(json_list)):
			order_items_var = orderitems()
			order_items_var.order_id = latest_id
			d = json_list[i]
			order_items_var.prod_name = d['prod_name']
			order_items_var.prod_count = d['prod_count']
			order_items_var.prod_base_qty = d['prod_base_qty']
			order_items_var.prod_price = d['prod_price']
			order_items_var.save()

		
		


		return HttpResponse("POSTED")
	return HttpResponse("ERROR")

@csrf_exempt
def send_sms(request):
	if request.method == 'POST':
		p = plivo.RestAPI(auth_id,auth_token)
		data = json.loads(request.body)
		mob_no = data['mobile_num']
		otp_code = data['otp']
		params = {
		'src':'PD-FRESCO',
		'dst':mob_no,
		'text':u"Your Fresco verification code is " + otp_code,
		'method':'POST'
		}
		response = p.send_message(params)
		return HttpResponse("OK")



	return HttpResponse("OK")



def past_orders(request,mob_no):
	queryset = order.objects.all()
	queryset = queryset.filter(mobile_num = mob_no)
	serializer = OrderSerializer(queryset,many=True)
	return JSONResponse(serializer.data)
