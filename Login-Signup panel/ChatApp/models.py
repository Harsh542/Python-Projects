from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Detail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    phone_no = models.TextField(unique=True)


class Cast(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    cast = models.TextField(blank=True, null=True)





