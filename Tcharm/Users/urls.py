from django.urls import path, include
from . import views

urlpatterns = [
    path("logreg/", views.ulogreg, name="logreg"),
    path("logout/", views.ulogout, name="logout"),
    path("tts/", include("TTS.urls")),
]