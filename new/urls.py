from django.urls import path
from rest_framework.routers import DefaultRouter

from new.views import SiteListAPIView, NewsAPIView, AdvertisingListApiView, AdminNews, AdminCreateImageNews, \
   AdminAdvertising, AdminSiteSettings

urlpatterns = [
   path("list/site",SiteListAPIView.as_view()),
   path("list/news",NewsAPIView.as_view()),
   path("list/advertesting",AdvertisingListApiView.as_view()),
   path("create/image/news",AdminCreateImageNews.as_view())
]

router = DefaultRouter()

router.register(r'news', AdminNews , basename='news')
urlpatterns += router.urls

router.register(r'advertising', AdminAdvertising , basename='advertising')
urlpatterns += router.urls

router.register(r'site', AdminSiteSettings , basename='site')
urlpatterns += router.urls
