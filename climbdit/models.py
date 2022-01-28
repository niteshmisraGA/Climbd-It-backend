from django.db import models

# Create your models here.

class Climber(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class State(models.Model):
    stateName = models.CharField(max_length=16)

    def __str__(self):
        return self.stateName


class Location(models.Model):
    locationName = models.CharField(max_length=128)
    stateName = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.locationName


class Climb(models.Model):
    climbName = models.CharField(max_length=16)
    climbGrade = models.CharField(max_length=8)
    climbDescription = models.CharField(max_length= 128)
    climbPic = models.ImageField(upload_to='images/', null = True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='climbs')
    climber = models.ForeignKey(Climber, on_delete=models.CASCADE, related_name='climbers')

    def __str__(self):
        return self.climbName
