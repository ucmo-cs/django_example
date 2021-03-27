from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cars.models import Cars
from cars.serializers import CarsSerializer

@csrf_exempt
def cars_list(request):
    """
    List all cars, or create a new cars.
    """
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def cars_detail(request, pk):
    """
    Retrieve, update or delete a cars.
    """
    try:
        cars = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarsSerializer(cars)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarsSerializer(cars, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cars.delete()
        return HttpResponse(status=204)

@csrf_exempt
def cars_model_list(request, tm):
    """
    List all cars of a certain make
    """
    if request.method == 'GET':
        cars = Cars.objects.filter(make__iexact=tm)
        serializer = CarsSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)
