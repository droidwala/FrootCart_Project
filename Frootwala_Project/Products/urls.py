from django.conf.urls import patterns,url
from Products import views


urlpatterns =[
              url(r'^(?P<types>\w+)/$',views.products_list),
              url(r'^search/(?P<prodname>\w+)/$',views.search_product),

 ]