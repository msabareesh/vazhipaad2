from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    # path('offeringsapi/', views.offeringsDataAPI),
    # path('createofferings/', views.createOfferings),
    # path('updateofferings/', views.updateOfferings),
    # path('deleteofferings/', views.deleteOfferings),
]
