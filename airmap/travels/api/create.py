from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from travels.utils.location import get_location
from travels.utils.timestamp import get_local_time


class TravelCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.data.get("travel_title")
        user = request.user

        if not travel_title:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
            )

        user.travel_set.create(
            travel_title=travel_title,
        )

        return Response(
            data={
                "travel_title": user.travel_set.last().travel_title,
                "id": user.travel_set.last().id,
            },
            status=status.HTTP_201_CREATED,
        )


class TravelDataCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        id = request.data.get("id")

        if not id:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
            )

        travel = request.user.travel_set.get(
                id=id,
        )

        image_metadatas = request.data.get("image_metadatas")

        if len(travel.travelimagedata_set.all()) + len(image_metadatas) > 30\
                or len(image_metadatas) > 10:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = request.user.email.split("@")

        for image_metadata in image_metadatas:
            timestamp = image_metadata.get("timestamp")
            latitude = image_metadata.get("latitude")
            longitude = image_metadata.get("longitude")

            address = get_location(latitude, longitude)
            country = address.get("country")
            city = address.get("city")

            created_date = get_local_time(timestamp)

            image_name = username[0] + "_" + id + "_" + timestamp + ".jpeg"

            metadata = travel.travelimagedata_set.create(
                user=request.user,
                latitude=latitude,
                longitude=longitude,
                timestamp=timestamp,
                created_date=created_date,
                travel_image_name=image_name,
                country=country,
                city=city,
            )

        return Response(
            status=status.HTTP_201_CREATED,
        )


class TravelImageCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILES.get("image_data")

        if not image:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
            )

        travel_image = request.user.travelimagedata_set.get(travel_image_name=image.name)

        travel_image.travel_image = image

        travel_image.save()
        return Response(
            status=status.HTTP_201_CREATED,
        )
