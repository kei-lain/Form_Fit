from django.db import models


class Workout(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    workout = models.CharField()
    targetArea = models.TextField()
    equipment = models.TextField()
    bodypart = models.TextField()
    instructions = models.TextField()
    