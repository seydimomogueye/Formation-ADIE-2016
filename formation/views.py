from  django.shortcuts import render
from  accounts import models



def formation(request, nom=''):
    heure = request.GET.get('heure', 'Pas d\'heure')
    participants = models.Account.objects.filter(account_type='1')
    inscriptions = models.Account.objects.all()

    return render(request, 'home.html', {'heure': heure, 'nom': nom,
                  'participants': participants,'inscriptions' : inscriptions})
