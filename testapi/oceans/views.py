from mongoengine import connect
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import detail_route
from .serializers import StationSerializer, ODataSerializer
from .models import Station, OData
from django.shortcuts import get_object_or_404, render
import json

connect("oceans", username="oceans", password="oceans")

def returnJsonError(status):
	if status == 404:
		return {"error": "Object Not Found"}
	elif status == 401:
		return {"error": "Not Authorized"}
	else:
		return {"error": "System Error"}

class StationViewSet(ModelViewSet):
	lookup_field = 'station_id'
	serializer_class = StationSerializer

	def get_queryset(self):
		return Station.objects.all()

	def retrieve(self, request, station_id=None):
		station = Station.objects(station_id=str(station_id))
		if len(station) == 0:
			return Response(returnJsonError(404), status=404)
		serializer = StationSerializer(station[0])
		return Response(serializer.data)

	@detail_route(methods=['get'])
	def sensors(self, request, station_id=None):
		sensor_data = OData.objects(station_id=station_id)
		if len(sensor_data) == 0:
			return Response(returnJsonError(404), status=404)
		serializer = ODataSerializer(sensor_data, many=True)
		return Response(serializer.data)
		def __doc__(self):
			return "Looks up senor data related to this station"
		

class ODataViewSet(ModelViewSet):
	lookup_field = "id"
	serializer_class = ODataSerializer

	def get_queryset(self):
		return OData.objects.all()


def index(request):
	return render(request, "index.html", {'stations': Station.objects.all()})

