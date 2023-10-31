from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framewrok import status
from django.http import Http404
from .models import Workout
from .serializers import WorkoutSerializer


class WorkoutList(APIView):
    def get(self,request, format=None):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = WorkoutSerializer(data=request.data) #post request pushing data from a form to the server
        if serializer.is_valid(): #if the data is good
            serializer.save() #save the item
            return Response(serializer.data, status=status.HTTP_201_Created)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)