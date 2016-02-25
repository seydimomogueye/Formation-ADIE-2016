from django.contrib import admin

from . import models


class AccountAdmin(admin.ModelAdmin):
    list_filter = ['fonction', 'sex', 'account_type']
    list_display  = ['user', 'fonction', 'sex', 'account_type']


admin.site.register(models.Account, AccountAdmin)


