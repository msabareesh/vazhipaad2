from rest_framework.generics import ListAPIView

from Orders.models import Order
from .serializers import OrderSerializer


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
