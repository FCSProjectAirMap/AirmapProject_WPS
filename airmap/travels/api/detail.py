from rest_framework.generics import ListAPIView

from travels.serializers import TravelDetailSerializer


class TravelDetailAPIView(ListAPIView):

    def get_queryset(self):
        travel = self.request.user.travel_set.get(id=self.kwargs.get("id"))
        return travel.imagemetadata_set.all().order_by("creation_data")
    serializer_class = TravelDetailSerializer
