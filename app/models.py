from django.db import models

from django.utils import timezone
import datetime
from django.db import migrations
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import json

# Create your models here.


class Banner(models.Model):
	banner = models.ImageField(upload_to='banners')
	titulo = models.CharField(max_length= 250, null=True, blank=True)
	subtitulo =  models.CharField(max_length=250, null=True, blank=True)




