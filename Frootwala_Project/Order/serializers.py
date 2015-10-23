from rest_framework import serializers
from Order.models import order

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = order
		fields = ('order_id','mobile_num','user_name','total_amt','del_day','del_time',
			'flat_no','building_name','locality_name','city_name',)