from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', default='uploads/default.png')
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    nickname = models.CharField(max_length=30, null=True, blank=True)
