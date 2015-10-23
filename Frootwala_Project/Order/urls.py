from django.conf.urls import patterns,url
from Order import views

urlpatterns =[
              url(r'^$',views.post_orders),
              url(r'^login/',views.send_sms),
              url(r'^(?P<mob_no>\w+)/$',views.past_orders),
 ]