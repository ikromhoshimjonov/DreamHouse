from django.urls import path
from rest_framework.routers import DefaultRouter
from home.views import AdminViewSetHome, AdminViewSetCity, AdminHomeImage, AdminAmenities, AmenitiesHomeCreateApiView, \
  AdminContact
from home.views import HomeListApiView, HomeFilterStatusType, HomeFilterStatusProperty, HomeFilterStatusHome, \
  HomeFilterCity, ListHomeMain, ListCityHome

urlpatterns = [
  path("list/home/",HomeListApiView.as_view()),
  path("list/status/",HomeFilterStatusType.as_view()),
  path("list/property/",HomeFilterStatusProperty.as_view()),
  path("list/status/home",HomeFilterStatusHome.as_view()),
  path("list/filter/city/home/<str:city>/",HomeFilterCity.as_view()),
  path("list/main/home/",ListHomeMain.as_view()),
  path("list/city/",ListCityHome.as_view()),
  path("create/aminities/home/",AmenitiesHomeCreateApiView.as_view()),
]


router = DefaultRouter()

router.register(r'home', AdminViewSetHome , basename='home')
urlpatterns += router.urls

router.register(r'city', AdminViewSetCity , basename='city')
urlpatterns += router.urls

router.register(r'home_image', AdminHomeImage , basename='home_image')
urlpatterns += router.urls

router.register(r'amenities', AdminAmenities , basename='amenities')
urlpatterns += router.urls

router.register(r'contact', AdminContact , basename='contact')
urlpatterns += router.urls