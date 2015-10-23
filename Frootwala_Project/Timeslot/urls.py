from django.conf.urls import patterns,url
from Timeslot import views

urlpatterns = [
               url(r'^$',views.alt_slot_list),
        ]