from django.db import models
from django.contrib.auth.models import User

class MyFiles(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    file = models.FileField(upload_to= 'upldfile/')