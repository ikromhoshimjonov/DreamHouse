from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import TextField, ImageField, CharField, Model, ForeignKey, CASCADE, SET_NULL, EmailField


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given phone number must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number,  password, **extra_fields)

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = CharField(max_length=255,null=True,blank=True)
    email = EmailField(max_length=255, unique=True)
    description = TextField(null=True,blank=True)
    image = ImageField(upload_to="user/image",null=True,blank=True)
    job = CharField(max_length=255,null=True,blank=True)
    phone = CharField(max_length=30,null=True,blank=True)
    location = CharField(max_length=255,null=True,blank=True)
    address = CharField(max_length=255,null=True,blank=True)
    web = CharField(max_length=255,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class SocialMedia(Model):
    facebook = CharField(max_length=255,null=True,blank=True)
    instagram = CharField(max_length=255,null=True,blank=True)
    twitter = CharField(max_length=255,null=True,blank=True)
    linkedin = CharField(max_length=255,null=True,blank=True)

    user = ForeignKey("authentication.User",on_delete=CASCADE,related_name="social")

class Wishlist(Model):
    user = ForeignKey("authentication.User",on_delete=CASCADE,related_name="wishlist")
    home = ForeignKey("home.Home",on_delete=SET_NULL,related_name='wishlist',null=True,blank=True)

