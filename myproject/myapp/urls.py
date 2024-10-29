from django.urls import path
from .views import hello_world
from .views import geocode_address

urlpatterns = [
    path('hello/', hello_world),
     path('geo/', geocode_address, name='geo'),
]