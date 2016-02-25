from __future__ import unicode_literals

from django.db import models

from accounts import models as account_mdl
from matiere import models as matiere_mdl


class Plan(models.Model):
    #titre = models.CharField(max_length=100)
    account = models.ForeignKey(account_mdl.Account)
    matiere = models.ForeignKey(matiere_mdl.Matiere)
    JOUR_TYPE_CHOICES = (('0', 'Lundi'), ('1', 'Mardi'),\
     	('2', 'Mercredi'),('3', 'Jeudi'),('4', 'Vendredi'),('5', 'Samedi'))
    
    jour_type = models.CharField(verbose_name="Jour de semaine", 
				    max_length=2, choices=JOUR_TYPE_CHOICES)
    debut = models.IntegerField()
    fin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __unicode__(self):
        return '{} {} {} {} {}'.format(self.matiere.titre, 
        	self.matiere.description,
        	self.jour_type_display,
        	self.debut_display+'h',
        	self.fin_display+'h' )
