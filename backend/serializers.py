from rest_framework import serializers
from .models import Workout
from authentication.models import Person


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['person','workout','targetArea','equipment','bodypart','instructions']
        
