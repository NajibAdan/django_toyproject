from django.db import models

class Features(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=300)
    is_true = models.BooleanField()