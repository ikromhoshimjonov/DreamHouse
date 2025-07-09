from django.urls import path

from home.views import HomeListApiView, HomeFilterStatusType, HomeFilterStatusProperty, HomeFilterStatusHome, \
  HomeFilterCity

urlpatterns = [
  path("list/home/",HomeListApiView.as_view()),
  path("list/status/",HomeFilterStatusType.as_view()),
  path("list/property/",HomeFilterStatusProperty.as_view()),
  path("list/status/home",HomeFilterStatusHome.as_view()),
  path("list/filter/city/home/<str:city>/",HomeFilterCity.as_view())
]
