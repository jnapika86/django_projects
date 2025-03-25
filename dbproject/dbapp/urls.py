from django.urls import path
from .views import item, additem
urlpatterns = [
    path('', item, name='item'),
    path('add/', additem, name='additem'),
]

