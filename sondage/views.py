# coding=utf8
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from . import forms


def sondage_list(request):
    sondages = models.Sondage.objects.all()
    return render(request, 'sondages/list.html', locals())


def sondage_add(request):
    if request.method == 'POST':
        form = forms.SondageForm(request.POST)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre avis a bien été pris en compte")
            return redirect(sondage_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    form = forms.SondageForm()

    return render(request, 'sondages/form.html', locals())


def sondage_edit(request, pk):
    sondage = get_object_or_404(models.Sondage, pk=pk)

    if request.method == 'POST':
        form = forms.SondageForm(request.POST, instance=sondage)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre avis a bien été pris en compte")
            return redirect(sondage_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    # sondage = models.Sondage.objects.get(pk=pk)
    form = forms.SondageForm(instance=sondage)

    return render(request, 'sondages/form.html', locals())


def sondage_delete(request, pk):
    sondage = get_object_or_404(models.Sondage, pk=pk)
    sondage.delete()
    messages.success(request, "L'avis a bien disparu, dans la nature...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
