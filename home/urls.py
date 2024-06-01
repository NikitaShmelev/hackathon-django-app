from django.urls import path
from .views import IndexView, PostCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("create/", PostCreateView.as_view(), name="create_post"),
]
