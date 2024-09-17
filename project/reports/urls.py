from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crisis.views import CrisisViewSet
from donations.views import DonationViewSet
from .views import ReportViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'crisis', CrisisViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
