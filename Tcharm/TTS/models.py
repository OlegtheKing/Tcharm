from django.db import models
from django.contrib.auth.models import User

class TTS(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfiles")
    file = models.FileField(upload_to="tts/")


