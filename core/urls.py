from django.urls import path
from core.views import *

urlpatterns = [
    path('control/', control, name='control'),
]
