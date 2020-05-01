from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from selectionsystem.selectionapp.use_cases.select_next_target import SelectNextTargetUseCase


class RadarSelection(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response(BufferError(), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        result = SelectNextTargetUseCase(request.data).execute()
        return Response(result.to_json(), status=status.HTTP_200_OK)
