from django.urls import path 
#from django.conf import settings
#from django.conf.urls.static import static
from dashboard import views # this imports views as a module. its functions are then called for the urls


urlpatterns = [
    path('result/', views.download, name='result'),
    path('index/', views.result_view, name='index'),
]

