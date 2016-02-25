from __future__ import unicode_literals

from django.db import models

#from accounts import models as account_mdl


class Matiere(models.Model):
    titre = models.CharField(max_length=100)
    #account = models.ForeignKey(account_mdl.Account)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __unicode__(self):
        return '{} {}'.format(self.titre, self.description)
