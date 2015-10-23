from django.db import models

class order(models.Model):
	order_id = models.AutoField(primary_key=True)
	mobile_num = models.CharField(max_length = 15)
	user_name = models.CharField(max_length = 50)
	total_amt = models.CharField(max_length = 10)
	del_day = models.CharField(max_length = 10)
	del_time = models.CharField(max_length = 15)
	flat_no = models.CharField(max_length = 10)
	building_name = models.CharField(max_length = 40)
	locality_name = models.CharField(max_length = 50)
	city_name = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.user_name


class orderitems(models.Model):
	order_id = models.IntegerField()
	prod_name = models.CharField(max_length = 40)
	prod_count = models.CharField(max_length = 10)
	prod_base_qty = models.CharField(max_length = 20)
	prod_price = models.CharField(max_length = 10)


	def __unicode__(self):
		return self.prod_name

