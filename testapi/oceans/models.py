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
	ID = IntField(db_field="-ID")

	metadata = EmbeddedDocumentField(StationMetadata)
	parameter = EmbeddedDocumentListField(StationParams)


	#this is to tell mongoengine to link us to the station collection
	meta = {"collection": "station", "allow_inheritance": True}


	def __str__(self):
		print("Station Buoy Name {0}".format(self.name))

	
class OceanProducts(EmbeddedDocument):
	meta = {'allow_inheritance': True}
	t = DateTimeField()
	f = StringField()
	name = StringField()
	v = FloatField()

class AirPressureProduct(OceanProducts):
	pass

class WaterTempProduct(OceanProducts):
	pass

class AirTempProduct(OceanProducts):
	pass

class WindProduction(OceanProducts):
	d = StringField()
	g = StringField()
	f = StringField()
	s = StringField()
	dr = StringField()


class OData(Document):
	station_id = IntField()
	loc = PointField()
	name = StringField()
	id = IntField()
	fetch_date = DateTimeField()
	products = EmbeddedDocumentListField(OceanProducts)

	#this is to tell mongoengine to link us to the ocean_data collection
	meta = {"collection": "ocean_data", 'allow_inheritance': True}
	def __str__(self):
		print("Ocean data point {0}".format(self.name))
	