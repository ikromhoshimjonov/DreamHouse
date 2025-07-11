from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from home.models import Home, City, HomeImage, Amenities, AmenitiesHome, Contact
from home.peginations import HomePagination, CityPagination
from home.serializers import HomeModelSerializer, HomeMainModelSerializer, CityHomeModelSerializer, \
    HomeImageModelSerializer, AdminAmenitiesModelSerializer, AmenitiesHomeModelSerializer, ContactModelViewSet
from is_super.super_user import IsSuperUser


@extend_schema(tags=["home"])
class HomeListApiView(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(sale=True)

@extend_schema(tags=["home"])
class HomeFilterStatusType(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get("status")
        return super().get_queryset().filter(status=status)

@extend_schema(tags=["home"])
class HomeFilterStatusProperty(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["property"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get("property")
        return super().get_queryset().filter(property=status)

@extend_schema(tags=["home"])
class HomeFilterStatusHome(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status_home"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get("status_home")
        return super().get_queryset().filter(status_home=status)

@extend_schema(tags=["home"])
class HomeFilterStatusHome(ListAPIView):
    serializer_class = HomeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status_home"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get("status_home")
        return super().get_queryset().filter(status_home=status)

@extend_schema(tags=["home"])
class HomeFilterCity(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        city = self.kwargs.get("city")
        return super().get_queryset().filter(city__name=city)

@extend_schema(tags=["home"])
class ListHomeMain(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeMainModelSerializer
    pagination_class = HomePagination
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["home"])
class ListCityHome(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityHomeModelSerializer
    pagination_class = CityPagination
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["home"])
class AdminViewSetHome(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer
    permission_classes = [IsAuthenticated,IsSuperUser]

@extend_schema(tags=["home"])
class AdminViewSetCity(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityHomeModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

@extend_schema(tags=["home"])
class AdminHomeImage(ModelViewSet):
    queryset = HomeImage.objects.all()
    serializer_class = HomeImageModelSerializer
    permission_classes = [IsAuthenticated,IsSuperUser]

@extend_schema(tags=["home"])
class AdminAmenities(ModelViewSet):
    queryset = Amenities.objects.all()
    serializer_class = AdminAmenitiesModelSerializer
    permission_classes = [IsAuthenticated,IsSuperUser]

@extend_schema(tags=["home"])
class AmenitiesHomeCreateApiView(CreateAPIView):
    queryset = AmenitiesHome.objects.all()
    serializer_class = AmenitiesHomeModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

@extend_schema(tags=["home"])
class AdminContact(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactModelViewSet
    permission_classes = [IsAuthenticated, IsSuperUser]