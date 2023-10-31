from django.db import models
from django.contrib.auth.model import User 

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    age = models.models.models.PositiveSmallIntegerField(min=18)
    ROLE_CHOICES = (
        (female, 'female'),
        (male, 'male'),
        (other , 'other'),

    )
    gender = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    fitnessgoal = models.TextField()