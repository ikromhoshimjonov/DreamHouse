from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from new.models import SiteSettings, News, Advertising
from new.serializers import SiteSettingsModelSerializer, NewsModelSerializer, AdvertisingModelSerializer


@extend_schema(tags=["news"])
class SiteListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsModelSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["news"])
class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["news"])
class AdvertisingListApiView(ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingModelSerializer
    permission_classes = [IsAuthenticated]

