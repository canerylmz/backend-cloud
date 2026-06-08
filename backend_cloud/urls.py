from django.urls import path
from image_api import views


urlpatterns = [
    path("", views.health, name="health"),
    path("get/resolution", views.get_resolution, name="get_resolution"),
    path("convert/grayscale", views.convert_grayscale, name="convert_grayscale"),
]
