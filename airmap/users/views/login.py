from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "login.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        next_url = request.POST.get("next_url") or reverse("login")  # FIXME: redirect to home

        user = authenticate(
            email=email,
            password=password,
        )

        if user:
            login(request, user)

            return redirect(next_url)

        return redirect(reverse("login"))
