from django.urls import path

from . import views

urlpatterns = [
    path('', views.random_puzzle, name='random_puzzle'),
    path('rate', views.rate, name='rate'),
    path('counter', views.trial, name='random_puzzle'),
]
