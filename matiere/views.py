# coding=utf8
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from . import forms


def matiere_list(request):
    matiere = models.Matiere.objects.all()
    return render(request, 'matieres/list.html', locals())


def matiere_add(request):
    if request.method == 'POST':
        form = forms.MatiereForm(request.POST)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre matiere a été enregistree avec succees")
            return redirect(matiere_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    form = forms.MatiereForm()

    return render(request, 'matieres/form.html', locals())


def matiere_edit(request, pk):
    matiere = get_object_or_404(models.Matiere, pk=pk)

    if request.method == 'POST':
        form = forms.MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre matiere a été enregistree avec succes")
            return redirect(matiere_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    # sondage = models.Sondage.objects.get(pk=pk)
    form = forms.MatiereForm(instance=matiere)

    return render(request, 'matieres/form.html', locals())


def matiere_delete(request, pk):
    matiere = get_object_or_404(models.Matiere, pk=pk)
    matiere.delete()
    messages.success(request, "La matiere a ete supprime avec succes...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
