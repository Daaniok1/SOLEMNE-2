from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^category/(?P<category_id>\d+)/$', views.category),
    url(r'^product/(?P<product_id>\d+)/$', views.product),
]