from django.db import models

from users.models import User


class Travel(models.Model):

    user = models.ForeignKey(User)

    travel_title = models.CharField(
        max_length=256,
    )
