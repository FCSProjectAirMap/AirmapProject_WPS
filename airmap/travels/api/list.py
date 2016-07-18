from rest_framework.generics import ListAPIView

from travels.serializers import TravelListSerializer


class TravelListAPIView(ListAPIView):

    def get_queryset(self):
        user = self.request.user
        return user.travel_set.all()
    serializer_class = TravelListSerializer
