from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'(?P<pk>\d+)/edit/', views.sondage_edit, name='sondage_edit'),
    url(r'(?P<pk>\d+)/delete/', views.sondage_delete, name='sondage_delete'),
    url(r'add/', views.sondage_add),
    url(r'', views.sondage_list),
)
