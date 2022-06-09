from django.urls import re_path as url
from store import views

urlpatterns = [
    url(r'^api/products$', views.product_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^api/clients$', views.client_list),
    url(r'^api/clients/(?P<pk>[0-9]+)$', views.client_detail),
    url(r'^api/brands$', views.brand_list),
    url(r'^api/brands/(?P<pk>[0-9]+)$', views.brand_detail),
]
