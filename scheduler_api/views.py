from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

from scheduler_app import models
from scheduler_api import serializers

class PersonViewset(viewsets.ModelViewSet):
    """Handle creating and updating viewsets"""
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)