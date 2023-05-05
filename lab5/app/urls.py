from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aircraft/', views.aircraft, name='aircraft'),
    path('price/', views.price, name='price'),
    path('contacts/', views.contacts, name='contacts'),
]
