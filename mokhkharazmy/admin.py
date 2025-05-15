from . import models
from django.contrib import admin  
from .models import Calculation  

class CalculationAdmin(admin.ModelAdmin):  
    list_display = ['user', 'shape_type', 'perimeter', 'area', 'created_at', 'updated_at']  
    list_filter = ['shape_type', 'created_at']  
    ordering = ['created_at']  
    readonly_fields = ['created_at', 'updated_at']  
    date_hierarchy = 'created_at'  

admin.site.register(Calculation, CalculationAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Product)