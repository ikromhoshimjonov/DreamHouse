from django.contrib import admin
from new.models import News, SiteSettings, Advertising, NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    pass