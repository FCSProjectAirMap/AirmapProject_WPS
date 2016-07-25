from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from travels.utils.location import get_location
from travels.utils.timestamp import get_local_time


class TravelDataCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.data.get("travel_title")

        travel = request.user.travel_set.get(
            travel_title=travel_title
        )

        if travel:
            pass
        else:
            travel = request.user.travel_set.create(
                travel_title=travel_title,
            )

        image_metadatas = request.data.get("image_metadatas")

        for image_metadata in image_metadatas:
            timestamp = image_metadata.get("timestamp")
            latitude = image_metadata.get("latitude")
            longitude = image_metadata.get("longitude")

            address = get_location(latitude, longitude)
            country = address.get("country")
            city = address.get("city")

            created_date = get_local_time(latitude, longitude, timestamp)

            image_name = timestamp + ".jpeg"

            metadata = travel.travelimagedata_set.create(
                user=request.user,
                latitude=latitude,
                longitude=longitude,
                timestamp=timestamp,
                create_date=created_date,
                travel_image_name=image_name,
            )

        return Response(
            status=status.HTTP_200_OK,
        )


class TravelImageCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILE.get("image")

        travel_image = request.user.travelimagedata_set.get(travel_image_name=request.FILE.get("filename"))

        image_upload = travel_image.create(
            image=image,
        )

        return Response(
            status=status.HTTP_200_OK,
        )
