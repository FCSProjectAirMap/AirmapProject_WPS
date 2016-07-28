from django.conf.urls import url

from travels.api import *


urlpatterns = [
        url(r'^list/', TravelListAPIView.as_view(), name='list'),
        url(r'^detail/(?P<id>\d+)/', TravelDetailAPIView.as_view(), name='detail'),
        url(r'^create_title/', TravelCreateAPIView.as_view(), name='title_create'),
        url(r'^create_data/', TravelDataCreateAPIView.as_view(), name='data_create'),
        url(r'^create_image/', TravelImageCreateAPIView.as_view(), name='image_create'),
        url(r'^delete/(?P<id>\d+)/', TravelDeleteAPIView.as_view(), name='delete'),
        ]
