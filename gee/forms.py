from django import forms
from earthengine.products import EE_PRODUCTS
from django.contrib.admin import widgets

# Initialize the platform options
platform_options = [
('modis', 'MODIS'),
('sentinel', 'Sentinel'),
('landsat', 'Landsat')]

REDUCTION_METHOD_CHOICES = (
	('median', 'median'),
	('mosaic', 'mosaic'),
	('mode', 'mode'),
	('mean', 'mean'),
	('minimum', 'min'),
	('maximum', 'max'),
	('sum', 'sum'),
	('count', 'count'),
	('product', 'product'),
	)

default_platform = 'modis'
default_sensors = EE_PRODUCTS[default_platform]
first_sensor_key = next(iter(default_sensors.keys()))
default_products = default_sensors[first_sensor_key]
first_product_key = next(iter(default_products.keys()))
first_product = default_products[first_product_key]


sensor_options = []
for sensor in default_sensors:
    sensor_options.append((sensor, sensor.upper()))

product_options = []
for product, info in default_products.items():
    product_options.append((product, info['display']))

class SatelliteDataForm(forms.Form):
	"""
	The satellite data form with the following fields
	"""
	platforms = forms.ChoiceField(choices = platform_options, 
		widget = forms.Select(attrs={'class':'form-control'}))

	sensors = forms.ChoiceField(choices = sensor_options, 
		widget = forms.Select(attrs={'class':'form-control'}))

	products = forms.ChoiceField(choices = product_options, 
		widget = forms.Select(attrs={'class':'form-control'}))

	reducer = forms.ChoiceField(choices = REDUCTION_METHOD_CHOICES, 
		widget = forms.Select(attrs={'class':'form-control'}))