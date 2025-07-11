from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from is_super.super_user import IsSuperUser
from new.models import SiteSettings, News, Advertising, NewsImage
from new.serializers import SiteSettingsModelSerializer, NewsModelSerializer, AdvertisingModelSerializer, NewsImageModel


@extend_schema(tags=["site"])
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

@extend_schema(tags=["news"])
class AdminNews(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

@extend_schema(tags=["news"])
class AdminCreateImageNews(CreateAPIView):
    queryset = NewsImage
    serializer_class = NewsImageModel
    permission_classes = [IsAuthenticated,IsSuperUser]

@extend_schema(tags=["news"])
class AdminAdvertising(ModelViewSet):
    queryset = Advertising
    serializer_class = AdvertisingModelSerializer
    permission_classes = [IsAuthenticated,IsSuperUser]

@extend_schema(tags=["site"])
class AdminSiteSettings(ModelViewSet):
    queryset = SiteSettings
    serializer_class = SiteSettingsModelSerializer
    permission_classes = [IsAuthenticated,IsSuperUser]
