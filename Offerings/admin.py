from django.contrib import admin
from Temple.models import *
from Offerings.models import *

# Register your models here.
admin.site.register(Temple)
admin.site.register(Temple_Offering)
admin.site.register(Idols)
admin.site.register(State)
admin.site.register(District)
admin.site.register(OfferingCategory)
admin.site.register(Offerings)
