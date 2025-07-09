from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import  ListAPIView
from rest_framework.permissions import IsAuthenticated
from home.models import Home
from home.serializers import HomeModelSerializer


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

