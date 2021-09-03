from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('helado/', helado, name='helado'),
    path('galletas/', galletas, name='galletas'),
    path('frutas/', frutas, name='frutas'),
    path('ensaladas/', ensaladas, name='ensaladas'),
    path('comidas/', comidas, name='comidas'),
    path('burritos/', burritos, name='burritos'),
]

