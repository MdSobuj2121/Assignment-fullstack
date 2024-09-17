from rest_framework import viewsets
from .models import Donation
from .serializers import DonationSerializer
from rest_framework.response import Response
class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DonationSerializer(queryset, many=True)
        return Response(serializer.data)
