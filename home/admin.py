from django.contrib import admin
from home.models import Home, Contact, City, AmenitiesHome, HomeImage, Amenities


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(AmenitiesHome)
class AmenitiesHomeAdmin(admin.ModelAdmin):
    pass

@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    pass
