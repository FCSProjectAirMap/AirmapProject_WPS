from django.db import models

from users.models import User


class TravelImageData(models.Model):

    user = models.ForeignKey(User)
    travel = models.ForeignKey("Travel")

    latitude = models.CharField(
        max_length=256,
    )
    longitude = models.CharField(
        max_length=256,
    )
    country = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )
    timestamp = models.CharField(
        max_length=256,
    )

    create_date = models.CharField(
        max_length=256,
    )

    travel_image_name = models.CharField(
        max_length=256,
    )

    travel_image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
