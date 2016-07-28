import os
from django.conf import settings

from geopy.geocoders import GoogleV3


def get_location(latitude, longitude):

    geolocator = GoogleV3(api_key=os.environ.get("GOOGLE_API_KEY"))

    location = geolocator.reverse("{latitude}, {longitude}".format(
        latitude=latitude,
        longitude=longitude,
    ))

    if len(location) > 1:
        address = location[0].address
        address_list = address.split(",")
        country = address_list[-1]
        city = address_list[-2]
    elif len(location) == 1:
        address == location[0].address
        address_list = address.split(",")
        country = address_list[-1]
        city = CITY_NULL_MESSAGE
    else:
        country = COUNTRY_NULL_MESSAGE
        city = CITY_NULL_MESSAGE

    result = {
        "country": country,
        "city": city,
    }

    return result
