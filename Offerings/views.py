from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import Temple_Offering_Serializer
from rest_framework.generics import ListAPIView

from .models import *


def index(request):
    return render(request, 'order_table.html')


def offeringsDataAPI(request):
    data = OfferingCategory.objects.all()
    #serializer_class = Temple_Offering_Serializer(data, many=True)
    dataList = []
    for i in data:
        dataList.append({'offering': i.offering_category_name,
                         'category': i.offering_type, 'id': i.id})
    #jsonopt = jsonpickle.encode(dataList)
    return JsonResponse(dataList, safe=False)


@csrf_exempt
def createOfferings(request):
    offering = request.POST.get('offering')
    category = request.POST.get('category')
    OfferingCategory.objects.create(
        offering_category_name=offering,
        offering_type=category,
    )
    return JsonResponse('Created Offering', safe=False)


@csrf_exempt
def updateOfferings(request):
    offeringID = request.POST.get('id')
    category = request.POST.get('category')
    offering = OfferingCategory.objects.get(id=offeringID)
    offering.offering_type = category
    print("pdate")
    print(offering)
    offering.save()
    return JsonResponse('updated Offering', safe=False)


@csrf_exempt
def deleteOfferings(request):
    offeringID = request.POST.get('id')
    offering = OfferingCategory.objects.get(id=offeringID)
    offering.delete()
