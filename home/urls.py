from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path("upload_file/", FileUploadView.as_view(), name="upload"),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    
    path("transfers/map/", TransferMapView.as_view(), name="transfer_map"),
    path('api/transfers/', transfers_json, name='transfers_json'),

    path('api/stops_near_location/', stops_near_location, name='stops_near_location'),
    path('api/transfers_json/', transfers_json, name='transfers_json'),
    path('api/transfers_for_stop/<int:stop_id>/', transfers_for_stop, name='transfers_for_stop'),
]
