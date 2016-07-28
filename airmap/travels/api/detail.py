from rest_framework.generics import ListAPIView

from travels.serializers import TravelDetailSerializer


class TravelDetailAPIView(ListAPIView):

    def get_queryset(self):
        travel = self.request.user.travel_set.get(id=self.kwargs.get("id"))
        return travel.travelimagedata_set.all().order_by("created_date")
    serializer_class = TravelDetailSerializer
