from rest_framework.serializers import ModelSerializer

from home.models import Home


class HomeModelSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = ("name" , "description" , "property_code" , "new_column","price","beds",
                  "baths","volume","build","garage","country","state","area","documents",
                  "latitude","longitude","date","status","property","status_home","city"
                  )