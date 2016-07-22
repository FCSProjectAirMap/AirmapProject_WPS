from django.db import models

from users.models import User


class TravelImageMetaData(models.Model):

    user = models.ForeignKey(User)
    travel = models.ForeignKey("Travel")
    image = models.OneToOneField("TravelImage")

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

    create_date = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
