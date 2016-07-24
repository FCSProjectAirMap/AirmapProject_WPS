from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from travels.utils.location import get_location
from travels.utils.timestamp import get_local_time


class TravelDataCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.data.get("travel_title")

        if travel_title in [
            travel_class.get("travel_title")
            for travel_class
            in request.user.travel_set.values()
        ]:
            travel = request.user.travel_set.get(
                travel_title=travel_title)
        else:
            travel = request.user.travel_set.create(
                travel_title=travel_title,
            )

        image_metadatas = request.data.get("image_metadatas")

        for image_metadata in image_metadatas:
            timestamp_data = image_metadata.get("timestamp")
            latitude_data = image_metadata.get("latitude")
            longitude_data = image_metadata.get("longitude")

            address = get_location(latitude_data, longitude_data)
            country = address.get("country")
            city = address.get("city")
            local_date = get_local_time(latitude_data, longitude_data, timestamp_data)

            image_name = timestamp_data + ".jpeg"

            metadata = travel.travelimagedata_set.create(
                user=request.user,
                latitude=latitude_data,
                longitude=longitude_data,
                timestamp=timestamp_data,
                create_date=local_date,
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
