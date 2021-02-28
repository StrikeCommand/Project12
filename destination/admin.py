from django.contrib import admin

from .models import Point, City


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'city', ('latitude', 'longitude'))


admin.site.register(City)
