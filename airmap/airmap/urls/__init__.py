from django.conf.urls import url, include
from django.contrib import admin

from users.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^signup/', SignupView.as_view(), name="signup"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),

    url(r'^api/', include("airmap.urls.api", namespace="api")),
    ]
