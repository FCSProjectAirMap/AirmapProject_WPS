from django.contrib.auth import get_user_model, authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SignupApi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        return Response(
                status=status.HTTP_403_FORBIDDEN
                )

    def post(self, request, *args, **kwargs):

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            validate_email(email)
        except ValidationError:
            return Response(
                    status=status.HTTP_403_FORBIDDEN
                    )

        user = authenticate(
                email=email,
                password=password
                )

        if not user:
            user = get_user_model().objects.create_user(
                    email=email,
                    password=password,
                    )
            return Response(
                    status=status.HTTP_200_OK,
                    )
        return Response(
                status=status.HTTP_403_FORBIDDEN
                )
