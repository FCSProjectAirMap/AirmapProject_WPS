from rest_framework import serializers
from travels.models import Travel


class TravelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = [
                "travel_title",
                "id",
                ]
