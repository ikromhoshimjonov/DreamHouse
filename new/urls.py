from django.urls import path

from new.views import SiteListAPIView, NewsAPIView, AdvertisingListApiView

urlpatterns = [
   path("list/site",SiteListAPIView.as_view()),
   path("list/news",NewsAPIView.as_view()),
   path("list/advertesting",AdvertisingListApiView.as_view())
]