var GEE_DATASETS = (function() {
    // Wrap the library in a package function
    "use strict"; // And enable strict mode for this library

    /************************************************************************
    *                      MODULE LEVEL / GLOBAL VARIABLES
    *************************************************************************/
    var MODIS = 'modis',
        SENTINEL = 'sentinel',
        LANDSAT = 'landsat',
        INITIAL_START_DATE,
        INITIAL_END_DATE,
        EE_PRODUCTS,
        THE_PRODUCTS;
    var m_map,
        m_gee_layer;


    var public_interface;

    // Selector Variables
    var m_platform,
        m_sensor,
        m_product,
        m_start_date,
        m_end_date,
        m_reducer;

    /************************************************************************
    *                    PRIVATE FUNCTION DECLARATIONS
    *************************************************************************/
    // Dataset Select Methods
    var bind_controls, update_product_options, update_sensor_options, update_date_bounds, collect_data;
    // Map Methods
    var update_map, update_data_layer, create_data_layer, clear_map;

    /************************************************************************
    *                    PRIVATE FUNCTION IMPLEMENTATIONS
    *************************************************************************/
    // Dataset Select Methods
    bind_controls = function() {
        $('#id_platforms').on('change', function() {
            let platform = $('#id_platforms').val();

            if (platform !== m_platform) {
                m_platform = platform;
                console.log(`Platform Changed to: ${m_platform}`);
                // Update the sensor options when platform changes
                update_sensor_options();
            }
        });

        $('#id_sensors').on('change', function() {
            let sensor = $('#id_sensors').val();

            if (sensor !== m_sensor) {
                m_sensor = sensor;
                console.log(`Sensor Changed to: ${m_sensor}`);
                // Update the product options when sensor changes
                update_product_options();
            }
        });

        $('#id_products').on('change', function() {
            let product = $('#id_products').val();

            if (product !== m_product) {
                m_product = product;
                console.log(`Product Changed to: ${m_product}`);
                // Update the valid date range when product changes
                update_date_bounds();
            }
        });


        $('#id_start_date').on('change', function() {
            let start_date = $('#id_start_date').val();

            if (start_date !== m_start_date) {
                m_start_date = start_date;
                $( "#id_end_date" ).attr("min", m_start_date);
                console.log(`Start Date Changed to: ${m_start_date}`);
            }
        });

        $('#id_end_date').on('change', function() {
            let end_date = $('#id_end_date').val();

            if (end_date !== m_end_date) {
                m_end_date = end_date;
                console.log(`End Date Changed to: ${m_end_date}`);
            }
        });

        $('#id_reducer').on('change', function() {
            let reducer = $('#id_reducer').val();

            if (reducer !== m_reducer) {
                m_reducer = reducer;
                console.log(`Reducer Changed to: ${m_reducer}`);
            }
        });

        /*$('#load_map').on('click', function() {
            update_map();
        });

        $('#clear_map').on('click', function() {
            clear_map();
        });*/


    };

    update_sensor_options = function() {
        if (!m_platform in THE_PRODUCTS) {
            alert('Unknown platform selected.');
        }

        // Clear sensor options
        $('#id_sensors').select2().empty();

        // Set the Sensor Options
        let first_option = true;
        for (var sensor in THE_PRODUCTS[m_platform]) {
            let sensor_display_name = sensor.toUpperCase();
            let new_option = new Option(sensor_display_name, sensor, first_option, first_option);
            $('#id_sensors').append(new_option);
            first_option = false;
        }

        // Trigger a sensor change event to update select box
        $('#id_sensors').trigger('change');
        update_date_bounds();
    };

    update_product_options = function() {
        if (!m_platform in THE_PRODUCTS || !m_sensor in THE_PRODUCTS[m_platform]) {
            alert('Unknown platform or sensor selected.');
        }

        // Clear product options
        $('#id_products').select2().empty();

        let first_option = true;

        // Set the Product Options
        for (var product in THE_PRODUCTS[m_platform][m_sensor]) {
            let product_display_name = THE_PRODUCTS[m_platform][m_sensor][product]['display'];
            let new_option = new Option(product_display_name, product, first_option, first_option);
            $('#id_products').append(new_option);
            first_option = false;
        }

        // Trigger a product change event to update select box
        $('#id_products').trigger('change');
        update_date_bounds();
    };
    update_date_bounds = function() {
        // Get new date picker bounds for the current product
        let earliest_valid_date = THE_PRODUCTS[m_platform][m_sensor][m_product]['start_date'];
        let latest_valid_date = THE_PRODUCTS[m_platform][m_sensor][m_product]['end_date'];
        console.log(latest_valid_date)
        $( "#id_start_date" ).attr("min", earliest_valid_date);
        console.log('Date Bounds Changed To: ' + earliest_valid_date + ' - ' + latest_valid_date);
    };

    /*collect_data = function() {
        let data = {
            platform: m_platform,
            sensor: m_sensor,
            product: m_product,
            start_date: m_start_date,
            end_date: m_end_date,
            reducer: m_reducer
        };
        return data;
    };
    // Map Methods
    update_map = function() {
    let data = collect_data();

    let xhr = $.ajax({
        type: 'POST',
        url: "{% url 'get-image-collection' %}",
        dataType: 'json',
        data: data
    });

    xhr.done(function(response) {
        if (response.success) {
            console.log(response.url);
            update_data_layer(response.url);
        } else {
            alert('Oops, there was a problem loading the map you requested. Please try again.');
        }
    });
};

    update_data_layer = function(url) {
    if (!m_gee_layer) {
        create_data_layer(response.url);
    } else {
        m_gee_layer.getSource().setUrl(url);
    }
};

    create_data_layer = function(url) {
    let source = L.tileLayer(response.url, {
            attribution: '&copy; <a href="https://www.earthengine.google.com">Google Earth Engine</a>'
        }).addTo(map);

    source.on('tileloadstart', function() {
        $('#loader').addClass('show');
    });

    source.on('tileload', function() {
        $('#loader').removeClass('show');
    });

    source.on('tileloaderror', function() {
        $('#loader').removeClass('show');
    });

    m_gee_layer = L.tileLayer({
        url: url,
        attribution: '&copy; <a href="https://www.earthengine.google.com">Google Earth Engine</a>'
    });

    // Insert below the draw layer (so drawn polygons and points render on top of the data layer).
    m_map.getLayers().insertAt(1, m_gee_layer);
};


    clear_map = function() {
    if (m_gee_layer) {
        m_map.removeLayer(m_gee_layer);
        m_gee_layer = null;
    }
};
*/



    /************************************************************************
    *                            PUBLIC INTERFACE
    *************************************************************************/
    public_interface = {};

    /************************************************************************
    *                  INITIALIZATION / CONSTRUCTOR
    *************************************************************************/
    $(function() {
        // Initialize Global Variables
        bind_controls();

        // Initialize Constants
        EE_PRODUCTS = $('#ee-products').data('ee-products');
        THE_PRODUCTS = JSON.parse(EE_PRODUCTS.replace(/'/g, '"'));
        console.log(THE_PRODUCTS);
        //EE_PRODUCTS = JSON.parse("{{ ee_products|safe }}");
        INITIAL_START_DATE = m_start_date = $('#id_start_date').val();
        INITIAL_END_DATE = m_end_date = $('#id_end_date').val();

        // Initialize members
        m_platform = $('#id_platforms').val();
        m_sensor = $('#id_sensors').val();
        m_product = $('#id_products').val();
        m_reducer = $('#id_reducer').val();
        m_start_date = $("#id_start_date").val();
        m_end_date = $("#id_end_date").val();
        m_map = map;
    });

    return public_interface;

}());// End of package wrapper