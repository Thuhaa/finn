import datetime as dt
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.core.serializers import serialize
import folium
import ee
import jsonify
import json
from earthengine.products import EE_PRODUCTS
from .forms import SatelliteDataForm
from earthengine.methods import get_image_collection_asset


def home_view(request):
    '''
    To prevent confusion of urls, here is a `home page` that will be loaded at the root
    '''
    return render(request, 'gee/index.html')


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

        print(platform, sensor, product, start_date, end_date, reducer)
        response_data.update({
            'success': True,
            'url': url,
            'products':product
        })
        #the_response_data = json.dumps(response_data)
        #print(the_response_data)
        return JsonResponse(response_data)