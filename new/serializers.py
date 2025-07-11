from rest_framework.serializers import ModelSerializer

from new.models import SiteSettings, News, Advertising, NewsImage


class SiteSettingsModelSerializer(ModelSerializer):
    class Meta:
        model = SiteSettings
        fields ="email" ,"phone_number","address"

class NewsModelSerializer(ModelSerializer):
    class Meta:
        model = News
        fields ="description" , "sales_department" , 'phone' ,"email"

class AdvertisingModelSerializer(ModelSerializer):
    class Meta:
        model = Advertising
        fields = "icon" ,

class NewsImageModel(ModelSerializer):
    class Meta:
        model = NewsImage
        fields = "image" , "news"
