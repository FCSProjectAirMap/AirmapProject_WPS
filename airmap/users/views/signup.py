from django.contrib.auth import get_user_model, authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic import View
from django.shortcuts import render


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "signup.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            validate_email(email)
        except ValidationError:
            pass

        user = authenticate(
                email=email,
                password=password
                )

        if not user:
            user = get_user_model().objects.create_user(
                    email=email,
                    password=password,
                    )
            pass
