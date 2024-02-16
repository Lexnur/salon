from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.login, name=''),
    path('register', views.register, name='register'),


]
