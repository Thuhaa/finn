from django import forms
from earthengine.products import EE_PRODUCTS
from django.contrib.admin import widgets
# Initialize the platform, sensor and product choices tuples with empty lists
PLATFORM_CHOICES = []
SENSOR_CHOICES = []
PRODUCT_CHOICES = []

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

TEST_CHOICES = (('this', 'this'),('that', 'that'),('then', 'then'))

# The following code tries to populate the form choices automatically from the data given in the products.py file
for platform in EE_PRODUCTS.keys():
	PLATFORM_CHOICES.append((platform, platform.upper()))
	
	for sensor in EE_PRODUCTS[platform].keys():
		SENSOR_CHOICES.append((sensor,sensor))

		for product in EE_PRODUCTS[platform][sensor].keys():
			PRODUCT_CHOICES.append(
				(product, 
				EE_PRODUCTS[platform][sensor][product]['display'])
				)


class SatelliteDataForm(forms.Form):
	"""
	The satellite data form with the following fields
	"""
	platforms = forms.ChoiceField(choices = PLATFORM_CHOICES, 
		widget = forms.Select(attrs={'class':'form-control'}))

	sensors = forms.ChoiceField(choices = SENSOR_CHOICES, 
		widget = forms.Select(attrs={'class':'form-control'}))

	products = forms.ChoiceField(choices = PRODUCT_CHOICES, 
		widget = forms.Select(attrs={'class':'form-control'}))

	reducer = forms.ChoiceField(choices = REDUCTION_METHOD_CHOICES, 
		widget = forms.Select(attrs={'class':'form-control'}))