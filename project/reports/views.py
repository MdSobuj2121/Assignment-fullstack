from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
from rest_framework.response import Response
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data)