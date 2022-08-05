from django.contrib import admin
from django.urls import path, include 
from . import views # this imports views as a module. its functions are then called for the urls


urlpatterns = [
    path('index/', views.file_upload_view, name='dashboard-index'),
]
