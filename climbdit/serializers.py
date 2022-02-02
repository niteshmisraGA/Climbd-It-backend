from rest_framework import serializers
from .models import Climb, Climber, Location, State
from django.contrib.auth.models import User

class StateSerializer(serializers.ModelSerializer):
    locations = serializers.StringRelatedField(many=True)
    class Meta:
        model = State
        fields = ['stateName', 'locations', 'id']

class LocationSerializer(serializers.ModelSerializer):
    climbs = serializers.StringRelatedField(many=True)
    # stateName = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location
        fields = ['stateName', 'climbs']


class ClimbSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Climb
        fields = ['climbName', 'climbGrade', 'climbDescription', 'climbPic', 'climber', 'location']

class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_supervisor(**validate_data)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']