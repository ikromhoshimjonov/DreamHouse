import json
import random
import smtplib
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from redis import  Redis
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from authentication.models import User, SocialMedia, Wishlist
from root.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST
from sender_mail.send_email import send_email


class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "email" , "password"
        write_only_fields = "password"

    def validate_email(self,value):
        random_number = random.randrange(10000, 99999)
        password_hash = make_password(self.initial_data.get("password"))
        # port = EMAIL_PORT
        # smtp_server = EMAIL_HOST
        # sender_email = EMAIL_HOST_USER
        # password = EMAIL_HOST_PASSWORD

        # with smtplib.SMTP_SSL(smtp_server, port) as server:
        #     server.login(sender_email, password)
        #     server.sendmail(sender_email, value, f"code = {random_number}")
        send_email(value,f"code {random_number}")

        data = {
            "email": value,
            "code": random_number,
            "password":password_hash
        }
        redis = Redis(decode_responses=True)
        str_data = json.dumps(data)
        redis.mset({value: str_data})
        redis.expire(value, time=timedelta(minutes=1))
        return value

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

class VerifySerializer(Serializer):
    email = EmailField(max_length=200)
    code = IntegerField()

    def validate_email(self,value):
        data_request = self.initial_data
        redis = Redis(decode_responses=True)
        datas_str = redis.get(value)
        if not datas_str:
            raise serializers.ValidationError({"message": "Bunday email mavjud emas tekshirib qaytadan kiriting !!!"})
        datas = json.loads(datas_str)
        code_random = datas.get("code")
        code = data_request.get("code")
        if str(code_random) == str(code):
            datas.pop("code")
            User.objects.create(**datas)
            return value
        raise serializers.ValidationError({"message":"Emailga junatgan kodni kiriting muammo bor !!!"})

class ForgetPasswordSerializer(Serializer):
    email = EmailField(max_length=255)

    def validate_email(self,value):
        if not  User.objects.filter(email=value):
            raise serializers.ValidationError({"message": "Bunday email mavjud emas tekshirib kiriting !!"})
        return value

    def send_mail(self):
        port = EMAIL_PORT
        smtp_server = EMAIL_HOST
        sender_email = EMAIL_HOST_USER
        password = EMAIL_HOST_PASSWORD
        email = self.data.get("email")
        message = f"""\
        Subject: Royxatdan otish havolasi

        Tasdiqlash havolangiz:
        http://localhost:8000/#/register/api_v1_change_create/?email={email}
        """

        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, email, message)

class ChangeSerializer(Serializer):
    new_password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)
    email = CharField(max_length=255)

    def validate_new_password(self,value):
        datas = self.initial_data
        confirm_password = datas.get("confirm_password")
        email = datas.get("email")
        if confirm_password == value:
            if  User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                user.password = make_password(value)
                user.save()
                return value
            raise serializers.ValidationError({"message":"Bunday email mavjud emas tug'ri kiritimg !! "})
        raise  serializers.ValidationError({"message":"Confirm password ni  tug'ri kiritimg !! "})