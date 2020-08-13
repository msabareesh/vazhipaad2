from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('offeringsapi/', views.offeringsDataAPI),
    path('createofferings/', views.createOfferings),
    path('updateofferings/', views.updateOfferings),
    path('deleteofferings/', views.deleteOfferings),
]
