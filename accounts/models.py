from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = (('0', 'Formateur'), ('1', 'Participant'))
    SEX_CHOICES = (('F', 'Feminin'), ('M', 'Masculin'))
    account_type = models.CharField(verbose_name="Type de compte", 
				    max_length=2, choices=ACCOUNT_TYPE_CHOICES)
    fonction = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'{}'.format(self.user.username)
