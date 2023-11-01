from django.urls import path

from . import views

urlpatterns = [
    path('create-user/', views.CreatePersonAPI.as_view()),
    path('update-user/', views.UpdatePersonAPI.as_view())
  
]
