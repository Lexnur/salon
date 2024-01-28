from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('women', views.index, name='index'),
    path('men', views.men, name='men'),
    path('junior', views.junior, name='junior'),


]