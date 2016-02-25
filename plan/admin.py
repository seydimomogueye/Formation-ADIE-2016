from django.contrib import admin

from . import models


class PlanAdmin(admin.ModelAdmin):
    list_filter = ['jour_type','debut','fin', 'created_at']
    list_display = ['debut','fin', 'created_at', 'updated_at']


admin.site.register(models.Plan, PlanAdmin)
