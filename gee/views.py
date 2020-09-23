import datetime as dt
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import folium
import ee
import jsonify
import json
from earthengine.products import EE_PRODUCTS
from .forms import SatelliteDataForm
from earthengine.methods import get_image_collection_asset

def map_view(request):
    '''
    This will be the mapview
    '''
    satellite_data_form = SatelliteDataForm()
    latest_date = dt.datetime.today().strftime('%Y-%m-%d')
    context =   {
    'satellite_data_form':satellite_data_form,
    'ee_products':EE_PRODUCTS,
    'latest_date':latest_date,
    }
    return render(request, 'gee/map.html', context)

def get_ee_data(request):
    '''
    This is the view to call earth engine data
    '''
    dataset = (ee.ImageCollection('MODIS/006/MOD13Q1')
        .filter(ee.Filter.date('2019-07-01', '2019-11-30'))
        .first())
    modisndvi = dataset.select('NDVI')

    vis_paramsNDVI = {
    'min': 0,
    'max': 9000,
    'palette': [ 'FE8374', 'C0E5DE', '3A837C','034B48',]}

    map_id_dict = ee.Image(modisndvi).getMapId(vis_paramsNDVI)

    tiles = map_id_dict['tile_fetcher'].url_format

    print(tiles)
    HttpResponse(tiles)


def get_image_collection(request):
    """
    Controller to handle image collection requests.
    """
    response_data = {'success': False}

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    else:
        platform = request.POST.get('platforms')
        sensor = request.POST.get('sensors')
        product = request.POST.get('products')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reducer = request.POST.get('reducer')

        url = get_image_collection_asset(
            platform=platform,
            sensor=sensor,
            product=product,
            date_from=start_date,
            date_to=end_date,
            reducer=reducer
        )

        response_data.update({
            'success': True,
            'url': url
        })
        return JsonResponse(response_data)
