from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'(?P<pk>\d+)/edit/', views.matiere_edit, name='matiere_edit'),
    url(r'(?P<pk>\d+)/delete/', views.matiere_delete, name='matiere_delete'),
    url(r'add/', views.matiere_add),
    url(r'matiere/', views.matiere_list),
)
