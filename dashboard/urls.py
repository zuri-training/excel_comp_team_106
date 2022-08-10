from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from excel_comp_team_106.dashboard import views # this imports views as a module. its functions are then called for the urls


urlpatterns = [
    path('index/', views.file_upload_view, name='dashboard-index'),
    path('result/', views.result_view, name='dashboard-index'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
