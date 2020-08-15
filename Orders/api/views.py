from rest_framework.generics import ListAPIView

from Orders.models import Order


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
