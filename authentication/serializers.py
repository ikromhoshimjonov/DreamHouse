import smtplib
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer
from authentication.models import User, SocialMedia, Wishlist
from root.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST

class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "email" , "password"

    def validate_password(self,value):
        password = make_password(value)
        return password

    def create(self, validated_data):
        data = self.data
        password = self.initial_data.get("password")
        data["password_not_hashed"] = password
        return  User.objects.create(**data)

class ForgetPasswordSerializer(Serializer):
    email = CharField(max_length=255)

    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError({"message":"Bunday emailga ega user mavjud emas"})
        return value


    def send_email(self):
        receiver_email = self.data.get("email")
        password_message = User.objects.filter(email=receiver_email).first().password_not_hashed

        port = EMAIL_PORT
        smtp_server = EMAIL_HOST
        sender_email = EMAIL_HOST_USER
        password = EMAIL_HOST_PASSWORD


        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email,f"Bu sizning passwordingiz = {password_message}")

class ChangePasswordSerializer(Serializer):
    old_password = CharField(max_length=255)
    new_password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)

    def validate_old_password(self,value):
        user = self.context["request"].user
        if not  user.check_password(value):
            raise serializers.ValidationError({"message":"Eski parolingiz mos kelmayapti !!"})
        return value

    def validate_new_password(self,value):
        data = self.initial_data
        confirm = data.get("confirm_password")
        if  not value == confirm:
            raise serializers.ValidationError({"message":"Yangi parolingiz tasdiqlash paroliga mos kelmayapt !!"})
        return value



    def password_update(self):
        user_id = self.context["request"].user.id
        data = self.data
        password_not_hashed = data.get("new_password")
        password = make_password(password_not_hashed)
        datas = {
            "password_not_hashed":password_not_hashed,
            "password":password
        }
        return User.objects.filter(id=user_id).update(**datas)

class RequireFieldsUser(ModelSerializer):
    class Meta:
        model = User
        fields = "description","image","job","phone","location","address","web","username","email"

class SocialMediaSerializer(ModelSerializer):
    class  Meta:
        model = SocialMedia
        fields = "facebook","instagram","twitter","linkedin" ,"user"

class SocialMediaUpdateSerializer(ModelSerializer):
    class  Meta:
        model = SocialMedia
        fields = "facebook","instagram","twitter","linkedin"

class WishlistModelSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "user","home"








