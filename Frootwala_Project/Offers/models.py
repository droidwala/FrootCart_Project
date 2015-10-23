from django.db import models

class Offers(models.Model):
	url = models.URLField()
	#offer_url = models.URLField()

	def __unicode__(self):
		return self.url

