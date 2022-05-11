from django.db import models
from django.contrib.auth.models import User

class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    clikc_power = models.IntegerField(default=0)