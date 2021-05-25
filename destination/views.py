from django.shortcuts import render
from rest_framework import generics

from .models import City, Point
from .serializers import PointSerializer, CitySerializer, ListCitySerializer


class CityView(generics.RetrieveAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ListCityView(generics.ListAPIView):
    serializer_class = ListCitySerializer
    queryset = City.objects.all()


class PointView(generics.RetrieveAPIView):
    serializer_class = PointSerializer
    queryset = Point.objects.all()

