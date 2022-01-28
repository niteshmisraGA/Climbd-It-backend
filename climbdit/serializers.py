from rest_framework import serializers
from .models import Climb, Climber, Location, State

class StateSerializer(serializers.ModelSerializer):
    locations = serializers.StringRelatedField(many=True)
    class Meta:
        model = State
        fields = ['stateName', 'locations']

class LocationSerializer(serializers.ModelSerializer):
    climbs = serializers.StringRelatedField(many=True)
    # stateName = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location
        fields = ['locationName','stateName', 'climbs']


class ClimbSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Climb
        fields = ['climbName', 'climbGrade', 'climbDescription', 'climbPic', 'climber', 'location']

class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = ['name']