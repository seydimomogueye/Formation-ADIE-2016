#coding=utf8
from django import forms

from . import models
#from accounts import models as account_mdl


# class SondageForm(forms.Form):
#     avis = forms.CharField(label='Avis', required=True,
#                            widget=forms.TextInput(attrs={'class': 'form-control'}))
#     account = forms.ChoiceField(label="Account", required=True,
#                                 widget=forms.Select(attrs={'class': 'form-control'}),
#                                 choices=account_mdl.Account.objects.all().values_list('id', 'user__username'))
#
#     def save(self):
#         return "J'ai sauvegardé"

class MatiereForm(forms.ModelForm):
    class Meta:
        model = models.Matiere
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
