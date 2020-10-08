from django.urls import path
from . import views
urlpatterns = [
path('map/', views.map_view, name='map'),
path('get-image-collection', views.get_image_collection, name='get-image-collection'),
]