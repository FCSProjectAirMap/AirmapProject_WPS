from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from users.api import *
from users.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^signup/', SignupView.as_view(),),
    url(r'^login/', LoginView.as_view(), name="login"),

    url(r'^api/signup/', SignupApi.as_view(), name='signup'),
    url(r'^api/login/', obtain_jwt_token),
    ]
