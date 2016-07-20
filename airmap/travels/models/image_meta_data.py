from django.db import models

from .travel import Travel


class ImageMetaData(models.Model):

    travel = models.ForeignKey(Travel)

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
    image = models.ImageField(
        blank=True,
        null=True,
    )
    imagedata = models.BinaryField(
        blank=Ture,
        null=True,
    )
    timestamp = models.CharField(
        max_length=256,
    )
    creation_date = models.DateTimeField()
    timezone_date = models.DateTimeField()

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "other url"
