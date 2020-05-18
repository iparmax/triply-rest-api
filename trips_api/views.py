from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers, models


class TripViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.TripsSerializer
    queryset = models.Trip.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("user_id", "email","origin",'destination','dep_time')
    