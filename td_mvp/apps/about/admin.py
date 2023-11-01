from django.contrib import admin

from .models import About, Geo


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_editable = ['position']


@admin.register(Geo)
class GeoAdmin(admin.ModelAdmin):
    pass
