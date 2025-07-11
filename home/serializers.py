from rest_framework.serializers import ModelSerializer

from home.models import Home, City, HomeImage, Amenities, AmenitiesHome, Contact


class HomeModelSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = ("name" , "description" , "property_code" , "price","beds",
                  "baths","volume","build","garage","country","state","area","documents",
                  "latitude","longitude","date","status","property","status_home","city"
                  )

class HomeMainModelSerializer(ModelSerializer):
    class Meta:
        model  = Home
        fields = "name" ,"price" , "beds" ,"baths" , "volume" ,"area"

class CityHomeModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "name","image"

class HomeImageModelSerializer(ModelSerializer):
    class Meta:
        model = HomeImage
        fields = "image" , "home"

class AdminAmenitiesModelSerializer(ModelSerializer):
    class Meta:
        model = Amenities
        fields = "name" ,

class AmenitiesHomeModelSerializer(ModelSerializer):
    class Meta:
        model = AmenitiesHome
        fields = "home" ,"amenities"

class ContactModelViewSet(ModelSerializer):
    class Meta:
        model = Contact
        fields = "name" , "email" , "phone" , "avatar"