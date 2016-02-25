from django.contrib import admin

from . import models


class MatiereAdmin(admin.ModelAdmin):
    list_filter = ['titre', 'created_at']
    list_display = ['titre', 'created_at', 'updated_at']


admin.site.register(models.Matiere, MatiereAdmin)
