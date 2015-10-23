from django.db import models

class Product(models.Model):
	prod_id = models.AutoField(primary_key=True)
	prod_name = models.CharField(max_length=30)
	prod_price= models.IntegerField()
	prod_type = models.CharField(max_length=10)
	prod_qty = models.CharField(max_length=10)
	prod_img_url = models.URLField()

	def __unicode__(self):
		return self.prod_name


# Create your models here.
