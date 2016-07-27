from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

from users.api import *
from travels.api import *


urlpatterns = [
        url(r'^signup/', SignupApi.as_view(), name='signup'),
        url(r'^login/', obtain_jwt_token),
        url(r'^travel/list/', TravelListAPIView.as_view(), name='travel_list'),
        url(r'^travel/detail/(?P<id>\d+)/', TravelDetailAPIView.as_view(), name='travel_detail'),
        url(r'^travel/create_travel/', TravelCreateAPIView.as_view(), name='travel_create'),
        url(r'^travel/create/', TravelDataCreateAPIView.as_view(), name='travel_create'),
        url(r'^travel/create_image/', TravelImageCreateAPIView.as_view(), name='travel_create'),
]
