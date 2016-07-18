from django.conf.urls import url
from django.contrib import admin

from users.api import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/signup/', SignupApi.as_view(), name='signup'),
]
