from .models import *
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

class StationLocationSerializer(EmbeddedDocumentSerializer):
	class Meta:
		model = StationLocation
		fields = ('lat', 'long', 'state')

class StationMetadataSerializer(EmbeddedDocumentSerializer):
	class Meta:
		model = StationMetadata
		fields = ('date_established')

class StationSerializer(DocumentSerializer):
	class Meta:
		model = Station
		depth = 2
		fields = "__all__"


class ODataSerializer(DocumentSerializer):
	class Meta:
		model = OData
		fields = "__all__"

