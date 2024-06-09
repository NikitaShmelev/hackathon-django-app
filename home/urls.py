from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    
    
    path("upload_file/", FileUploadView.as_view(), name="upload"),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    
    path("", TransferMapView.as_view(), name="transfer_map"),
    path('api/transfers/', transfers_json, name='transfers_json'),

    path('api/stops_near_location/', stops_near_location, name='stops_near_location'),
    path('api/transfers_json/', transfers_json, name='transfers_json'),
    path('api/transfers_for_stop/<int:stop_id>/', transfers_for_stop, name='transfers_for_stop'),
    # path('api/find_route/', find_route, name='find_route'),
    # path('api/get_stop_by_name/<srt:name>/', get_stop_by_name, name='get_stop_by_name'),
]
