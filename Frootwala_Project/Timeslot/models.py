from django.db import models

class Slots(models.Model):
	slot = models.CharField(max_length=50)
	day = models.CharField(max_length=15)
	

	def __unicode__(self):
		return self.slot

