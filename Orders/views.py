from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from .utils import cookieCart, cartData
# Create your views here.


def store(request):
    cartdata = cartData(request)
    items = cartdata['items']
    order = cartdata['order']
    cartItems = cartdata['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'Orders/order_list.html', context)


def cart(request):
    cartdata = cartData(request)
    items = cartdata['items']
    order = cartdata['order']
    cartItems = cartdata['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # print(cartItems)
    return render(request, 'Orders/order_cart.html', context)


def checkout(request):
    cartdata = cartData(request)
    items = cartdata['items']
    order = cartdata['order']
    cartItems = cartdata['cartItems']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # print(cartItems)
    return render(request, 'Orders/order_checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    #print(productId, action, user)
    customer = Customer.objects.get(user_id=user.id)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
