from django.urls import path

from .views import ListCityView, CityView, PointView

urlpatterns = [
    path('cities/', ListCityView.as_view(), name='cities'),
    path('cities/<int:pk>', CityView.as_view(), name='city-details'),
    path('points/<int:pk>', PointView.as_view(), name='point-details'),
]