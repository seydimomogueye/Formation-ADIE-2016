from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib import messages

from  accounts import models
from accounts import forms

# Create your views here.



def inscription_list(request):
    inscriptions = models.Account.objects.all()
    return render(request, 'list_inscription.html', locals())


def inscription_add(request):
    if request.method == 'POST':
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre inscription a bien été pris en compte")
            return redirect(inscription_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    form = forms.InscriptionForm()

    return render(request, 'form_inscription.html', locals())


def inscription_edit(request, pk):
    inscription = get_object_or_404(models.Account, pk=pk)

    if request.method == 'POST':
        form = forms.InscriptionForm(request.POST, instance=inscription)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre inscription a bien été pris en compte")
            return redirect(inscription_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    # inscriptions = models.Inscription.objects.get(pk=pk)
    form = forms.InscriptionForm(instance=inscription)

    return render(request, 'form_inscription.html', locals())


def inscription_delete(request, pk):
    inscription = get_object_or_404(models.Account, pk=pk)
    inscription.delete()
    messages.success(request, "L'inscription a bien disparu, dans la nature...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
