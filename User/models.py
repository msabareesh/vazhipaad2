from django.contrib.auth.models import AbstractUser
from django.db import models
from Temple.models import Temple
# Create your models here.


class User(AbstractUser):
    temple_admin = models.BooleanField(null=True, blank=True)
    temple_staff = models.BooleanField(null=True, blank=True)
    customer_normal = models.BooleanField(null=True, blank=True)
    customer_premium = models.BooleanField(null=True, blank=True)
    user_image = models.ImageField(blank=True,
                                   null=True,
                                   upload_to='pics',
                                   verbose_name='IMAGE',)
    temple_name = models.ForeignKey(
        Temple, null=True, blank=True, on_delete=models.SET_NULL)
