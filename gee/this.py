import datetime as dt
from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import SelectInput, DatePicker, Button
from .gee.products import EE_PRODUCTS


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    default_platform = 'modis'
    default_sensors = EE_PRODUCTS[default_platform]
    first_sensor_key = next(iter(default_sensors.keys()))
    default_products = default_sensors[first_sensor_key]
    first_product_key = next(iter(default_products.keys()))
    first_product = default_products[first_product_key]

    # Build initial platform control
    platform_select = SelectInput(
        name='platform',
        display_text='Satellite Platform',
        options=(
            ('modis', 'MODIS'),
            ('sentinel', 'Sentinel'),
            ('landsat', 'Landsat')
        )
    )

    # Build initial sensor control
    sensor_options = []

    for sensor in default_sensors:
        sensor_options.append((sensor.upper(), sensor))

    sensor_select = SelectInput(
        name='sensor',
        display_text='Sensor',
        options=sensor_options
    )

    # Build initial product control
    product_options = []
    for product, info in default_products.items():
        product_options.append((info['display'], product))

    product_select = SelectInput(
        name='product',
        display_text='Product',
        options=product_options
    )

    # Hardcode initial end date to today (since all of our datasets extend to present)
    today = dt.datetime.today()
    initial_end_date = today.strftime('%Y-%m-%d')

    # Initial start date will a set number of days before the end date
    # NOTE: This assumes the start date of the dataset is at least 30+ days prior to today
    initial_end_date_dt = dt.datetime.strptime(initial_end_date, '%Y-%m-%d')
    initial_start_date_dt = initial_end_date_dt - dt.timedelta(days=30)
    initial_start_date = initial_start_date_dt.strftime('%Y-%m-%d')

    # Build date controls
    first_product_start_date = first_product.get('start_date', None)
    first_product_end_date = first_product.get('end_date', None) or initial_end_date

    start_date = DatePicker(
        name='start_date',
        display_text='Start Date',
        format='yyyy-mm-dd',
        start_view='decade',
        today_button=True,
        today_highlight=True,
        start_date=first_product_start_date,
        end_date=first_product_end_date,
        initial=initial_start_date,
        autoclose=True
    )

    end_date = DatePicker(
        name='end_date',
        display_text='End Date',
        format='yyyy-mm-dd',
        start_view='decade',
        today_button=True,
        today_highlight=True,
        start_date=first_product_start_date,
        end_date=first_product_end_date,
        initial=initial_end_date,
        autoclose=True
    )

    # Build reducer method control
    reducer_select = SelectInput(
        name='reducer',
        display_text='Reduction Method',
        options=(
            ('Median', 'median'),
            ('Mosaic', 'mosaic'),
            ('Mode', 'mode'),
            ('Mean', 'mean'),
            ('Minimum', 'min'),
            ('Maximum', 'max'),
            ('Sum', 'sum'),
            ('Count', 'count'),
            ('Product', 'product'),
        )
    )

    # Build Buttons
    load_button = Button(
        name='load_map',
        display_text='Load',
        style='default',
        attributes={'id': 'load_map'}
    )

    context = {
        'platform_select': platform_select,
        'sensor_select': sensor_select,
        'product_select': product_select,
        'start_date': start_date,
        'end_date': end_date,
        'reducer_select': reducer_select,
        'ee_products': EE_PRODUCTS,
        'load_button': load_button,
    }

    return render(request, 'earth_engine/home.html', context)
