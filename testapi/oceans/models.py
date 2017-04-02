#from django.db import models
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

class StationLocation(EmbeddedDocument):
	lat = FloatField()
	long = FloatField()
	state = StringField()

class StationMetadata(EmbeddedDocument):
	location = EmbeddedDocumentField(StationLocation)
	date_established = DateTimeField()

class StationParams(EmbeddedDocument):
	name = StringField(db_field="-name")
	sensorID = StringField(db_field="-sensorID")
	DCP = StringField(db_field="-DCP")
	status = StringField(db_field="-status")

class Station(Document):
	name = StringField(db_field="-name")
	station_id = StringField(db_field="-ID")

	metadata = EmbeddedDocumentField(StationMetadata)
	parameter = DynamicField()


	#this is to tell mongoengine to link us to the stations collection
	meta = {"collection": "stations"}


	def __str__(self):
		return "Station Buoy Name {0}".format(self.name)

	


class OData(Document):
	pid = ObjectIdField(db_field="_id")
	station_id = IntField()
	loc = PointField()
	name = StringField()
	senor_id = IntField(db_field="id")
	fetch_date = DateTimeField()
	products = DynamicField()
	lat = FloatField()
	lon = FloatField()
	#this is to tell mongoengine to link us to the ocean_data collection
	meta = {"collection": "ocean_data"}
	def __str__(self):
		print("Ocean data point {0}".format(self.name))
	