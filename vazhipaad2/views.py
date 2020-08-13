from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def activity_log_view(request):
    return render(request, 'user_activity_log.html')


def order_view(request):
    return render(request, 'Orders/order_table.html')
