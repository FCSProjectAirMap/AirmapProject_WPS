from rest_framework import serializers
from travels.models import ImageMetaData


class TravelDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageMetaData
        fields = [
                "creation_data",
                "latitude",
                "longitude",
                "country",
                "city",
                "timestamp",
                "image",
                ]
