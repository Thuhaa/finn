//Declare the variables
var INITIAL_START_DATE,INITIAL_END_DATE,EE_PRODUCTS,THE_PRODUCTS;
var platform,sensor,product,reducer,start_date,end_date;
var updated_sensor, updated_product;
//Grab the data div
EE_PRODUCTS = $('#ee-products').data('ee-products');

//Convert the products into a JSON object
THE_PRODUCTS = JSON.parse(THE_PRODUCTS = JSON.parse(EE_PRODUCTS.replace(/'/g, '"'));

platform = $('#id_platforms').val();
sensor = $('#id_sensors').val();
product = $('#id_products').val();
reducer = $('#id_reducer').val();
start_date = $('#id_start_date');
end_date = $('id_end_date').val();