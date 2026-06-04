
from django.urls import path
from . import views
#localhost:8000/ironman
urlpatterns = [
    path('', views.ironman, name = 'all_ironman'),
    
]
