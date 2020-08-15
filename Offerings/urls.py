from django.urls import path
from .views import OfferingListView, offeringsDataAPI, createOfferings, updateOfferings, deleteOfferings, index

app_name = 'offerings'

urlpatterns = [
    path('', index),
    path('offeringsapi/', offeringsDataAPI),
    path('createofferings/', createOfferings),
    path('updateofferings/', updateOfferings),
    path('deleteofferings/', deleteOfferings),
    path('TempleOfferingsAPI/', OfferingListView.as_view(),
         name='Temple-Offering-API'),
]
