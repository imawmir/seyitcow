from django.shortcuts import render
from django.http import HttpResponse
from example_app.models import users

# Create your views here.

def index(request):
    return render(request, 'index.html')

def User(request):

    user_list = users.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'user.html', context=user_dict)
