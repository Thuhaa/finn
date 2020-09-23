import ee


def mask_l8_sr(image):
    """
    Cloud Mask for Landsat 8 surface reflectance. Derived From: https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_SR
    """
    # Bits 3 and 5 are cloud shadow and cloud, respectively.
    cloudShadowBitMask = (1 << 3)
    cloudsBitMask = (1 << 5)

    # Get the pixel QA band.
    qa = image.select('pixel_qa')

    # Both flags should be set to zero, indicating clear conditions.
    mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0).And(qa.bitwiseAnd(cloudsBitMask).eq(0))
    return image.updateMask(mask)


def cloud_mask_l457(image):
    """
    Cloud Mask for Landsat 7 surface reflectance. Derived From: https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_SR
    """
    qa = image.select('pixel_qa')

    # If the cloud bit (5) is set and the cloud confidence (7) is high
    # or the cloud shadow bit is set (3), then it's a bad pixel.
    cloud = qa.bitwiseAnd(1 << 5).And(qa.bitwiseAnd(1 << 7)).Or(qa.bitwiseAnd(1 << 3))

    # Remove edge pixels that don't occur in all bands
    mask2 = image.mask().reduce(ee.Reducer.min())

    return image.updateMask(cloud.Not()).updateMask(mask2)


def mask_s2_clouds(image):
    """
    Cloud Mask for Sentinel 2 surface reflectance. Derived from: https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2
    """
    qa = image.select('QA60')

    # Bits 10 and 11 are clouds and cirrus, respectively.
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11

    # Both flags should be set to zero, indicating clear conditions.
    mask = qa.bitwiseAnd(cloudBitMask).eq(0).And(qa.bitwiseAnd(cirrusBitMask).eq(0))

    return image.updateMask(mask).divide(10000)
