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

    def get_local_time(self):
        from travels.utils.timestamp import get_local_time\
            as get_local_time_timestamp
        return get_local_time_timestamp(self.latitude, self.longitude, self.timestamp)
    local_time = property(get_local_time)

    def get_location(self):
        from travels.utils.location import get_location\
            as get_location_data
        return get_location_data(self.latitude, self.longitude)
    location = property(get_location)
