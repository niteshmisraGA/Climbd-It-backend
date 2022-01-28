from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClimberSerializer, ClimbSerializer, StateSerializer, LocationSerializer
from .models import Climber, Climb, State, Location
# Create your views here.

class ClimberViewSet(viewsets.ModelViewSet):
    queryset = Climber.objects.all()
    serializer_class = ClimberSerializer
    #auth goes here

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ClimbViewSet(viewsets.ModelViewSet):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer   