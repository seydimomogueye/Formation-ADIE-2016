# coding=utf8
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from . import forms


def plan_list(request):
    plan = models.Plan.objects.all()
    return render(request, 'plans/list.html', locals())


def plan_add(request):
    if request.method == 'POST':
        form = forms.PlanForm(request.POST)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre planification a été enregistree avec succees")
            return redirect(plan_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    form = forms.PlanForm()

    return render(request, 'plans/form.html', locals())


def plan_edit(request, pk):
    plan = get_object_or_404(models.Plan, pk=pk)

    if request.method == 'POST':
        form = forms.PlanForm(request.POST, instance=plan)
        if form.is_valid():
            value = form.save()
            messages.success(request, "Votre planification a été enregistree avec succes")
            return redirect(plan_list)
        else:
            messages.error(request, "Formulaire Invalide", extra_tags="danger")

    # sondage = models.Sondage.objects.get(pk=pk)
    form = forms.PlanForm(instance=plan)

    return render(request, 'plans/form.html', locals())


def plan_delete(request, pk):
    plan = get_object_or_404(models.Plan, pk=pk)
    plan.delete()
    messages.success(request, "La planification a ete supprime avec succes...")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
