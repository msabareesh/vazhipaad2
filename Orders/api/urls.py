from django.urls import path
from .views import OrderListAPIView

app_name = 'orders'
urlpatterns = [
    path('', OrderListAPIView.as_view(), name='api-order'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('offeringsapi/', views.offeringsDataAPI),
    # path('createofferings/', views.createOfferings),
    # path('updateofferings/', views.updateOfferings),
    # path('deleteofferings/', views.deleteOfferings),
]
