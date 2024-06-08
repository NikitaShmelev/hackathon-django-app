from django.urls import path
from .views import IndexView, PostCreateView, FileUploadView


urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path('upload_file/', FileUploadView.as_view(), name='upload'),
]
