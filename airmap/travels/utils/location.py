import os
from django.conf import settings

from geopy.geocoders import GoogleV3


def get_location(latitude, longitude):

    geolocator = GoogleV3(api_key=os.environ.get("GOOGLE_API_KEY"))

    location = geolocator.reverse("{latitude}, {longitude}".format(
        latitude=latitude,
        longitude=longitude,
    ))

    if not location:
        result = {
            "country": None,
            "city": None,
        }
        return result

    elements = location[0].raw.get("address_components")

    address_components = [
        {
            element.get("types")[0]: element.get("long_name"),
        }
        for element
        in elements
    ]
    address_dict = {}
    for address_component in address_components:
        for key, value in address_component.items():
            address_dict[key] = value

    if address_dict.get("locality"):
        city = address_dict.get("locality")
    city = address_dict.get("administrative_area_level_1")
    country = address_dict.get("country")

    result = {
        "country": country,
        "city": city,
    }

    return result
