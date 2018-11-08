from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.get_new_url(), name='get_new_url')
]