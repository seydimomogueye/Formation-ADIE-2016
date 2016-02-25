from django.contrib import admin

from . import models


class SondageAdmin(admin.ModelAdmin):
    list_filter = ['account', 'created_at']
    list_display = ['account', 'avis', 'created_at', 'updated_at']


admin.site.register(models.Sondage, SondageAdmin)
