from django.urls import path
from .views import IndexView, PostCreateView, FileUploadView

from .views import ShapeMapView, shapes_json, stops_json

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path("upload_file/", FileUploadView.as_view(), name="upload"),
    path("map/", ShapeMapView.as_view(), name="shape_map"),
    path("api/shapes/", shapes_json, name="shapes_json"),
    path("api/stops/", stops_json, name="stops_json"),
    path('upload_file/', FileUploadView.as_view(), name='upload'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),

]
