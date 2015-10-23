from rest_framework import serializers
from Products.models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('prod_id','prod_name','prod_price','prod_type','prod_qty','prod_img_url',)
		