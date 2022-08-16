from django.urls import path 
from Accounts import views # this imports views as a module. its functions are then called for the urls


urlpatterns = [
    path('', views.home, name='Accounts-home'), # this is the url to our home page
    path('register/', views.RegisterView.as_view(), name='Accounts-register'), # this defines the urls path for register
    path('profile/', views.profile, name='Accounts-profile'),

]
