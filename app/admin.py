from django.contrib import admin
from . models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'UGPA', 'RCN', 'TOEFL', 'LOR', 'SOP', 'HIGH_SCHOOL_POINTS', 'STATUS')
    
admin.site.register(Data, DataAdmin)
