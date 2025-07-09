from django.http import JsonResponse
from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.models import User, SocialMedia, Wishlist
from authentication.serializers import RegisterModelSerializer, ForgetPasswordSerializer, ChangePasswordSerializer, \
    RequireFieldsUser, SocialMediaSerializer, SocialMediaUpdateSerializer, WishlistModelSerializer


@extend_schema(tags=["register"])
class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

@extend_schema(tags=['login'], request=ForgetPasswordSerializer)
class ForgetPasswordCreateAPIView(APIView):
      permission_classes = [IsAuthenticated]
      def post(self, request):
          serializer = ForgetPasswordSerializer(data=request.data)
          if serializer.is_valid():
              serializer.send_email()
              return JsonResponse({"message": "Mofaqiyatli tastiqlandi"})
          return JsonResponse({"errors": serializer.errors.get("email")})

@extend_schema(tags=['login'], request=ChangePasswordSerializer)
class ChangePasswordAPIView(APIView):
    def post(self,request):
        serializer = ChangePasswordSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.password_update()
            return JsonResponse({"message": "Mofaqiyatli tastiqlandi"})
        return JsonResponse({"errors": serializer.errors})
    permission_classes = [IsAuthenticated,]

@extend_schema(tags=["login"])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@extend_schema(tags=["login"])
class CustomTokenRefreshView(TokenRefreshView):
    pass

@extend_schema(tags=["user"])
class CreateUserFields(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RequireFieldsUser
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

@extend_schema(tags=["user"])
class ListUserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RequireFieldsUser
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

@extend_schema(tags=["user"])
class CreateSocial(CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["user"])
class SocialUpdateAPI(UpdateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaUpdateSerializer
    permission_classes = [IsAuthenticated]

    def update(self,*args,**kwargs):
        pk = self.kwargs.get("pk")
        data = self.request.data
        if not SocialMedia.objects.filter(user_id=pk).exists():
            raise serializers.ValidationError({"message":"Bunday user mavjud emas"})
        SocialMedia.objects.filter(user_id=pk).update(**data)
        return  Response({"message":"Foydalanuvchi malumotlari uzgartirildi"})

@extend_schema(tags=["user"])
class WishlistListCreateView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       return super().get_queryset().filter(user=self.request.user)

@extend_schema(tags=["user"])
class WishlistDestroyApi(DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return super().get_queryset().filter(id=pk,user=self.request.user)



