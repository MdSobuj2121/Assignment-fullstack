from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Crisis
from .serializers import CrisisSerializer

class CrisisViewSet(viewsets.ModelViewSet):
    queryset = Crisis.objects.all()
    serializer_class = CrisisSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CrisisSerializer(queryset, many=True)
        return Response(serializer.data)
