from django.urls import path
from .views import *


urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path('upload_file/', FileUploadView.as_view(), name='upload'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('stops/<str:route_id>/', stops_for_route, name='stops_for_route'),
    path('shape/<str:route_id>/', shape_for_route, name='shape_for_route'),
    path('routes/<str:stop_id>/', routes_for_stop, name='routes_for_stop'),
]
