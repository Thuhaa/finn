import datetime as dt

EE_PRODUCTS = {
    'modis': {
        'terra': {
            'snow': {
                'display': 'Snow Cover Daily Global 500m',
                'collection': 'MODIS/006/MOD10A1',
                'index': 'NDSI_Snow_Cover',
                'vis_params': {
                    'min': 0.0,
                    'max': 100.0,
                    'palette': ['black', '0dffff', '0524ff', 'ffffff'],
                },
                'start_date': '2000-02-24',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'temperature': {
                'display': 'Land Surface Temperature and Emissivity Daily Global 1km',
                'collection': 'MODIS/006/MOD11A1',
                'index': 'LST_Day_1km',
                'vis_params': {
                    'min': 13000.0,
                    'max': 16500.0,
                    'palette': [
                        '040274', '040281', '0502a3', '0502b8', '0502ce', '0502e6',
                        '0602ff', '235cb1', '307ef3', '269db1', '30c8e2', '32d3ef',
                        '3be285', '3ff38f', '86e26f', '3ae237', 'b5e22e', 'd6e21f',
                        'fff705', 'ffd611', 'ffb613', 'ff8b13', 'ff6e08', 'ff500d',
                        'ff0000', 'de0101', 'c21301', 'a71001', '911003'
                    ],
                },
                'start_date': '2000-03-05',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            }
        },
    },
    'sentinel': {
        '5': {
            'cloud': {
                'display': 'Cloud',
                'collection': 'COPERNICUS/S5P/OFFL/L3_CLOUD',
                'index': 'cloud_fraction',
                'vis_params': {
                    'min': 0,
                    'max': 0.95,
                    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
                },
                'start_date': '2018-07-04',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'co': {
                'display': 'Carbon Monoxide',
                'collection': 'COPERNICUS/S5P/OFFL/L3_CO',
                'index': 'CO_column_number_density',
                'vis_params': {
                    'min': 0,
                    'max': 0.05,
                    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
                },
                'start_date': '2018-06-28',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'ozone': {
                'display': 'Ozone',
                'collection': 'COPERNICUS/S5P/OFFL/L3_O3',
                'index': 'O3_column_number_density',
                'vis_params': {
                    'min': 0.12,
                    'max': 0.15,
                    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
                },
                'start_date': '2018-09-08',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'so2': {
                'display': 'Sulphur Dioxide',
                'collection': 'COPERNICUS/S5P/OFFL/L3_SO2',
                'index': 'SO2_column_number_density',
                'vis_params': {
                    'min': 0.0,
                    'max': 0.0005,
                    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
                },
                'start_date': '2018-12-05',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'ch4': {
                'display': 'Methane',
                'collection': 'COPERNICUS/S5P/OFFL/L3_CH4',
                'index': 'CH4_column_volume_mixing_ratio_dry_air',
                'vis_params': {
                    'min': 1750,
                    'max': 1900,
                    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
                },
                'start_date': '2019-02-08',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
        }
    },
    'landsat': {
        '7': {
            'surface': {
                'display': 'Surface Reflectance',
                'collection': 'LANDSAT/LE07/C01/T1_SR',
                'index': '',
                'vis_params': {
                    'bands': ['B3', 'B2', 'B1'],
                    'min': 0,
                    'max': 3000,
                    'gamma': 1.4,
                },
                'cloud_mask': 'cloud_mask_l457',
                'start_date': '1999-01-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'evi': {
                'display': '8-day Enhanced Vegetation Index (EVI)',
                'collection': 'LANDSAT/LE07/C01/T1_8DAY_EVI',
                'index': 'EVI',
                'vis_params': {
                    'min': 0.0,
                    'max': 1.0,
                    'palette': [
                        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
                        '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
                        '012E01', '011D01', '011301'
                    ],
                },
                'start_date': '1999-01-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'ndwi': {
                'display': '8-day Normalized Difference Water Index (NDWI)',
                'collection': 'LANDSAT/LE07/C01/T1_8DAY_NDWI',
                'index': 'NDWI',
                'vis_params': {
                    'min': 0.0,
                    'max': 1.0,
                    'palette': ['0000ff', '00ffff', 'ffff00', 'ff0000', 'ffffff'],
                },
                'start_date': '1999-01-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
        },
        '8': {
            'surface': {
                'display': 'Surface Reflectance',
                'collection': 'LANDSAT/LC08/C01/T1_SR',
                'index': '',
                'vis_params': {
                    'bands': ['B4', 'B3', 'B2'],
                    'min': 0,
                    'max': 3000,
                    'gamma': 1.4,
                },
                'cloud_mask': 'mask_l8_sr',
                'start_date': '2013-04-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'ndvi': {
                'display': '8-day Normalized Difference Vegetation (NDVI)',
                'collection': 'LANDSAT/LC08/C01/T1_8DAY_NDVI',
                'index': 'NDVI',
                'vis_params': {
                    'min': 0.0,
                    'max': 1.0,
                    'palette': [
                        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
                        '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
                        '012E01', '011D01', '011301'
                    ],
                },
                'start_date': '2013-04-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
            'ndsi': {
                'display': '8-day Normalized Difference Snow Index (NDSI)',
                'collection': 'LANDSAT/LC08/C01/T1_8DAY_NDSI',
                'index': 'NDSI',
                'vis_params': {
                    'palette': ['000088', '0000FF', '8888FF', 'FFFFFF'],
                },
                'start_date': '2013-04-01',
                'end_date': str(dt.datetime.today().strftime("%Y-%m-%d"))  # to present
            },
        }
    }
}
