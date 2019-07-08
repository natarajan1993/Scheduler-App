from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import Http404

from scheduler_app import models
from scheduler_api import serializers

class PersonViewset(viewsets.ModelViewSet):
    """Handle creating and updating viewsets"""
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EventViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = models.Event.objects.all()
        serializer = serializers.EventSerializer(queryset, many = True, context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = serializers.EventSerializer(event)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return Response({'error':'record not found'})
        return Response(status=status.HTTP_204_NO_CONTENT)
