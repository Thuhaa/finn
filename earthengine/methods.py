from .products import EE_PRODUCTS
import logging
import ee
from ee.ee_exception import EEException
from . import cloud_mask as cm
from . import params as gee_account




if gee_account.service_account:
    try:
        credentials = ee.ServiceAccountCredentials(gee_account.service_account, gee_account.private_key)
        ee.Initialize(credentials)
    except EEException as e:
        print(str(e))
else:
    try:
        ee.Initialize()
    except EEException as e:
        from oauth2client.service_account import ServiceAccountCredentials
        credentials = ServiceAccountCredentials.from_p12_keyfile(
            service_account_email='',
            filename='',
            private_key_password='notasecret',
            scopes=ee.oauth.SCOPE + ' https://www.googleapis.com/auth/drive '
        )
        ee.Initialize(credentials)

def image_to_map_id(image_name, vis_params={}):
    """
    Get map_id parameters
    """
    try:
        ee_image = ee.Image(image_name)
        map_id = ee_image.getMapId(vis_params)
        tile_url = map_id['tile_fetcher'].url_format
        return tile_url

    except EEException as e:
        logging.error('An error occurred while attempting to retrieve the map id.', e)


def get_image_collection_asset(platform, sensor, product, date_from=None, date_to=None, reducer='median'):
    """
    Get tile url for image collection asset.
    """
    ee_product = EE_PRODUCTS[platform][sensor][product]

    collection = ee_product['collection']
    index = ee_product['index']
    vis_params = ee_product['vis_params']
    #cloud_mask = ee_product.get('cloud_mask', None)
    try:
        ee_collection = ee.ImageCollection(collection)

        if date_from and date_to:
            ee_filter_date = ee.Filter.date(date_from, date_to)
            ee_collection = ee_collection.filter(ee_filter_date)

        if index:
            ee_collection = ee_collection.select(index)
        '''
        if cloud_mask:
            cloud_mask_func = getattr(cm, cloud_mask, None)
            if cloud_mask_func:
                ee_collection = ee_collection.map(cloud_mask_func)
        '''
        if reducer:
            ee_collection = getattr(ee_collection, reducer)()

        tile_url = image_to_map_id(ee_collection, vis_params)

        return tile_url

    except EEException as e:
        logging.error("The following exception occured", e)
