from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^inscriptions(?P<pk>\d+)/edit/', views.inscription_edit, name='inscription_edit'),
    url(r'^inscriptions(?P<pk>\d+)/delete/', views.inscription_delete, name='inscription_delete'),
    url(r'^inscriptions/add/', views.inscription_add),
    url(r'^inscriptions', views.inscription_list),     
)
