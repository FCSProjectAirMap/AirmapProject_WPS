from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from travels.utils import MakeLocalData


class TravelCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.data.get("travel_title")
        travel = request.user.travel_set.create(
            travel_title=Travel_title
        )


class ImageMetadataCreateAPIView(APIView, MakeLocalData):

    def post(self, request, *args, **kwargs):

        imgae_metadatas = request.data.get("image_metadatas")

        for image_metadata in image_metadatas:
            creation_date = image_metadata.get("creation_date")
            timestamp = image_metadata.get("timesstamp")
            latitude = image_metadata.get("latitude")
            longitude = image_metadata.get("longitude")

            country = get_location(latitude, longitude)["country"]
            city = get_location(latitude, longtitude)["city"]

            metadata = request.travel.imagemetadata_set.create(
                creation_date=creation_date,
                latitude=latitude,
                longitude=longitude,
                country=country,
                city=city,
                timestamp=timestamp,
            )

        return Response(
                status=status.HTTP_200_OK,
                )


class ImageDataCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILES.get("image")

        travel_image = request.imagemetadata.imagedata_set.create(
                travel_image=image,
            )
