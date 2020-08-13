from django.db import models
from Temple.models import Temple

# Create your models here.


class OfferingCategory(models.Model):
    offering_category_name = models.CharField(
        max_length=120, null=False, blank=False)
    offering_type = models.CharField(max_length=120, null=False, blank=False)
    offering_category_added_date = models.DateField(auto_now_add=True)
    offering_category_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.offering_category_name


class Offerings(models.Model):
    offering_name = models.CharField(max_length=120, null=False, blank=False)
    offering_cat = models.ForeignKey(
        OfferingCategory, on_delete=models.CASCADE)
    offering_added_date = models.DateField(auto_now_add=True)
    offering_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.offering_name


class Temple_Offering(models.Model):
    offering_id = models.ForeignKey(
        Offerings, null=True, blank=False, on_delete=models.SET_NULL)
    offering_temple_name = models.ForeignKey(
        Temple, on_delete=models.CASCADE)
    offering_price = models.IntegerField(null=False, blank=False)
    prasadam_needed = models.BooleanField(default=True)
    offering_details_added_date = models.DateField(auto_now_add=True)
    offering_details_updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.offering_id)
