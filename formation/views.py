from django.http import HttpResponse
from django.shortcuts import render

from  accounts import models


def formation(request, nom=''):
    heure = request.GET.get('heure', 'Pas d\'heure')
    participants = models.Account.objects.filter(account_type='1')
    return render(request, 'home.html', {'heure': heure, 'nom': nom, 
                  'participants': participants})
