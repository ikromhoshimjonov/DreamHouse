from django.urls import path
from authentication.views import RegisterCreateAPIView, CustomTokenObtainPairView, CustomTokenRefreshView, \
    ChangePasswordAPIView, CreateUserFields, ListUserApiView, CreateSocial, \
    SocialUpdateAPI, WishlistListCreateView, WishlistDestroyApi, VerifyApiView, ForgetPasswordAPIView, ChangeAPIView
from django.conf.urls.static import static
from root import settings


# Auth
urlpatterns = [
   path("register/",RegisterCreateAPIView.as_view()),
   path("change/password/",ChangePasswordAPIView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# logic
urlpatterns +=[
    path("create/require/user/", CreateUserFields.as_view()),
    path("list/user/", ListUserApiView.as_view()),
    path("create/social", CreateSocial.as_view()),
    path("update/social/<int:pk>/", SocialUpdateAPI.as_view()),
    path("wishlist/create/list", WishlistListCreateView.as_view()),
    path("wishlist/delete/<int:pk>/", WishlistDestroyApi.as_view()),
    path("verify/",VerifyApiView.as_view()),
    path("forget/",ForgetPasswordAPIView.as_view()),
    path("change",ChangeAPIView.as_view())
]

# JWT
urlpatterns += [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]