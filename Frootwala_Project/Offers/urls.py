from django.conf.urls import patterns,url
from Offers import views

urlpatterns = [
              url(r'^$',views.offers_list),
	]
