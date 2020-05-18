from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from . import serializers, models

@permission_classes((IsAdminUser,))
class TripViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.TripsSerializer
    queryset = models.Trip.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("user_id", "email","origin",'destination','dep_time')
    