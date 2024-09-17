from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = InventorySerializer(queryset, many=True)
        return Response(serializer.data)
