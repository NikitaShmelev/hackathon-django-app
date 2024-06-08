from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path("upload_file/", FileUploadView.as_view(), name="upload"),
    path("map/", ShapeMapView.as_view(), name="shape_map"),
    path("api/shapes/", shapes_json, name="shapes_json"),
    path("api/stops/", stops_json, name="stops_json"),
    path("transfers/map/", TransferMapView.as_view(), name="transfer_map"),
    # path("transfers/api/transfers/", transfers_json, name="transfers_json"),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('api/stops_near_location/', stops_near_location, name='stops_near_location'),
]
