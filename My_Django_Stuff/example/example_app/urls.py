from django.urls import path,include
from example_app import views

urlpatterns = [
    path('', views.User, name='users'),
]
