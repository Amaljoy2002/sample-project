from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'post_list.html', {})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]