from django.conf import settings

from geopy.geocoders import GoogleV3


class MakeLocalData(GoogleV3):

    def get_location(latitude, longitude):

        geolocator = GoogleV3(api_key=os.environ.get("GOOGLE_API_KEY"))

        location = geolocator.reverse("{latitude}, {longitude}".format(
            latitude=latitude,
            longitude=longitude,
        ))

        address = location[0].address
        address_list = address.split(",")
        country = address_list[-1]
        city = address_list[-2]

        result = {
            "country": country,
            "city": city,
        }

        return result
