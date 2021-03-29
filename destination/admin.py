from django.contrib import admin

from .models import Point, City, PointImage


class PointImageInline(admin.TabularInline):
    model = PointImage
    extra = 1


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'city', ('latitude', 'longitude'))
    inlines = [PointImageInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name', ('latitude', 'longitude'))
