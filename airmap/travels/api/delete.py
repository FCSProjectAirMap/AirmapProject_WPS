from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TravelDeleteAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        travel = self.request.user.travel_set.get(id=self.kwargs.get("id"))
        imagedata = travel.travelimagedata_set.all()
        travel.delete()
        imagedata.delete()

        return Response(
                status=status.HTTP_200_OK,
                )
