from django.urls import path
from admin.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('trocarsenha/', trocarsenha, name='trocarsenha'),

    path('users/', users, name='list-users'),
    path('newuser/', newuser, name='new-user'),
    path('edituser/<int:id>', edituser, name='edit-user'),
    path('deleteuser/<int:id>', deleteuser, name='delete-user'),

    path('lares/', lares, name='list-lares'),
    path('newlar/', newlar, name='new-lar'),
    path('editlar/<int:id>', editlar, name='edit-lar'),
    path('deletelar/<int:id>', deletelar, name='delete-lar'),

    path('paciente/<int:id>', paciente, name='paciente'),
    path('lar/<int:id>', lar, name='lar'),

    path('pacientes/', pacientes, name='list-pacientes'),
    path('newpaciente/', newpaciente, name='new-paciente'),
    path('editpaciente/<int:id>', editpaciente, name='edit-paciente'),
    path('deletepaciente/<int:id>', deletepaciente, name='delete-paciente'),

    path('newvisita/<int:id>', newvisita, name='new-visita'),
    path('editvisita/<int:id>/<int:visita>', editvisita, name='edit-visita'),
    path('daletevisita/<int:id>/<int:visita>', deletevisita, name='delete-visita'),

    path('logs/', logs, name='logs'),
]
