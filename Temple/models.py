from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Idols(models.Model):
    idol_name = models.CharField(max_length=120, null=False, blank=False)
    idol_gender = models.CharField(max_length=120, null=False, blank=False)
    idol_added_date = models.DateField(auto_now_add=True)
    idol_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.idol_name


class State(models.Model):
    state_name = models.CharField(max_length=120, null=False, blank=False)
    state_added_date = models.DateField(auto_now_add=True)
    state_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.state_name


class District(models.Model):
    district_name = models.CharField(max_length=120, null=False, blank=False)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    district_added_date = models.DateField(auto_now_add=True)
    district_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.district_name


class Temple(models.Model):
    temple_name = models.CharField(max_length=120, null=False, blank=False)
    temple_status = models.CharField(
        max_length=120, null=False, blank=False, default="Active")
    temple_description = models.TextField(
        max_length=200, null=True, blank=True)
    temple_place = models.CharField(max_length=120, null=False, blank=False)
    temple_city = models.CharField(max_length=120, null=False, blank=False)
    temple_district = models.ForeignKey(District, on_delete=models.CASCADE)
    temple_state = models.ForeignKey(State, on_delete=models.CASCADE)
    temple_PINCode = models.IntegerField(null=False, blank=False)
    temple_image = models.ImageField(blank=False,
                                     null=False,
                                     upload_to='pics',
                                     verbose_name='IMAGE',)
    temple_icon = models.ImageField(blank=False,
                                    null=False,
                                    upload_to='pics',
                                    verbose_name='IMAGE',)
    temple_mail = models.CharField(max_length=120, null=False, blank=False)
    temple_phone = models.CharField(max_length=20, null=False, blank=False)
    temple_main_idol = models.ForeignKey(
        Idols, on_delete=models.CASCADE)
    temple_added_date = models.DateField(auto_now_add=True)
    temple_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.temple_name

    def get_absolute_url(self):
        return reverse("temples:Temple-Details", kwargs={"id": self.id})
