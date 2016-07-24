from rest_framework import serializers
from travels.models import TravelImageData


class TravelDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelImageData
        fields = [
                "creation_data",
                "latitude",
                "longitude",
                "country",
                "city",
                "timestamp",
                "image",
                ]
