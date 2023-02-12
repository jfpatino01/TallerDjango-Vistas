from django.shortcuts import render
from .logic import logic_measurments as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurements_dto = ml.get_measurement(id)
            measurements = serializers.serialize('json', [measurements_dto,])
            return HttpResponse(measurements, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        measurements_dto = ml.create_measurement(json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurements_dto = ml.get_measurement(pk)
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

    if request.method == 'PUT':
        measurements_dto = ml.update_measurement(pk, json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

    if request.method == 'DELETE':
        measurements_dto = ml.delete_measurement(pk)
        return HttpResponse('se borro :(')