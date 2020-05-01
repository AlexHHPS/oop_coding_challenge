from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from selectionsystem.selectionapp.use_cases.select_next_target import SelectNextTargetUseCase


class RadarSelection(APIView):
    def get(self, request, format=None):
        return Response("Operation not supported", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        if request.data.get("protocols") is None:
            return Response("Field protocols is missing", status=status.HTTP_400_BAD_REQUEST)

        if request.data.get("scan") is None:
            return Response("Scan protocols is missing", status=status.HTTP_400_BAD_REQUEST)

        result = SelectNextTargetUseCase(request.data).execute()
        return Response(result.to_dict(), status=status.HTTP_200_OK)
