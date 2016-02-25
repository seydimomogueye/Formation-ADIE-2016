from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'(?P<pk>\d+)/edit/', views.plan_edit, name='plan_edit'),
    url(r'(?P<pk>\d+)/delete/', views.plan_delete, name='plan_delete'),
    url(r'add/', views.plan_add),
    url(r'plan/', views.plan_list),
)
