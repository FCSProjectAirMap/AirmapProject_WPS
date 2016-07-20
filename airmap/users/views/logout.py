from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.chortcuts import redirect
from django.views.generic import views


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("login"))
