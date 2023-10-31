from django.urls import path
from .views import CreatePersonAPI, UpdatePersonAPI, 

urlpatterns = [
    path('create_user/', CreatePersonAPI.as_view()),
    path('update-user', UpdatePersonAPI.as_view()),
  
]
