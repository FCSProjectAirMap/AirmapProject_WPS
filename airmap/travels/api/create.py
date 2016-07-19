from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from geopy.geocoders import GoogleV3


class TravelCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.data.get("travel_title")
        travel = request.user.travel_set.create(
            travel_title=travel_title
        )

        geolocator = GoogleV3(api_key="GOOGLEV3_API_KEY")

        image_metadatas = request.data.get("image_metadatas")

        for image_metadata in image_metadatas:
            creation_date = image_metadata.get("creation_date")
            latitude = image_metadata.get("latitude")
            longitude = image_metadata.get("longitude")
            timestamp = image_metadata.get("timesstamp")
            image = image_metadata.get("image")

            location = geolocator.reverse("{latitude}, {longitude}".format(latitude=latitude, longitude=longitude))
            point = location[0]
            address = point.address
            address_list = address.split(",")
            country = address_list[-1]
            city = address_list[-2]

            metadata = request.travel.imagemetadata_set.create(
                creation_date=creation_date,
                latitude=latitude,
                longitude=longitude,
                country=country,
                city=city,
                timestamp=timestamp,
                image=image,
            )

        return Response(
                status=status.HTTP_200_OK,
                )
