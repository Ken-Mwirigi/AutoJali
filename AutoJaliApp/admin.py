
from django.contrib import admin
# Register your models here.

from AutoJaliApp.models import CarOwners,BreakDownDetails,Order

admin.site.register(CarOwners)
admin.site.register(BreakDownDetails)
admin.site.register(Order)

