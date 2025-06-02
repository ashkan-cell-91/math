# urls.py  
from django.contrib import admin  
from django.urls import path, include  
from .views import home
from . import views  # اطمینان حاصل کنید که views.py در همان دایرکتوری است  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),
    path('calculate/', views.calculate_shape, name='calculate_shape'),
    path('calculater/', views.calculater, name='calculater'),
    path('register/', views.register, name='register'),
    path('search/', views.search_data, name='search_data'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
