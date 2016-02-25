from __future__ import unicode_literals

from django.db import models

from accounts import models as account_mdl


class Sondage(models.Model):
    avis = models.CharField(max_length=200)
    account = models.ForeignKey(account_mdl.Account)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __unicode__(self):
        return '{} {}'.format(self.account.user.username, self.avis)
