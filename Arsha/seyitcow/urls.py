from django.urls import path
from seyitcow import views

# TEMPLATE URLS
app_name = 'seyitcow'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('animal/', views.animal, name='animal'),
]