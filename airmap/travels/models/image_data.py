import datetime
import os

from django.db import models

from users.models import User


def set_filename(now, instance, filename):
    return "{username}_{date}_{microsecond}{extension}".format(
        username=instance.user.email.split("@")[0],
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def user_directory_path(instance, filename):
    now = datetime.datetime.now()

    path = "image/{username}/{travel_title}/{filename}".format(
        username=instance.user.email,
        travel_title=instance.travel.travel_title,
        filename=set_filename(now, instance, filename),
    )

    return path


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
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    timestamp = models.CharField(
        max_length=256,
    )

    created_date = models.CharField(
        max_length=256,
    )

    travel_image_name = models.CharField(
        max_length=256,
        unique=True,
    )

    travel_image = models.ImageField(
        blank=True,
        null=True,
        upload_to=user_directory_path,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
