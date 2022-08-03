from django.urls import path,include
from AppTwo import views

urlpatterns = [
    path('', views.users, name='users'),
]
