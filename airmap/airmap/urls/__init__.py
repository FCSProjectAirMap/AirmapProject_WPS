from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from users.api import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^signup/', SignupApi.as_view(), name='signup'),
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),

    url(r'^travel/', include("airmap.urls.travel", namespace="travel")),
    ]
