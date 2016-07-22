from django.db import models

from users.models import User


class TravelImage(models.Model):

    user = models.ForeignKey(User)
    travel = models.ForeignKey("Travel")
    image = models.OneToOneField("TravelImageMetaData")

    travel_image_title = models.CharField(
        max_length=256,
    )
    travel_image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
