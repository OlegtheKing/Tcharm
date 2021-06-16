from django.urls import path
from . import views


urlpatterns = [
    path("", views.saved, name="saved"),
    path("convert/", views.converttoaudio, name="convert"),
    # path("download/<str:filepath>", views.download, name="download"),
]