from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient/new/$', views.patient_new, name='patient_new'),
    url(r'^patient/new/fraction/$', views.fraction_new, name='fraction_new'),
    url(r'^patient/list/$', views.patient_list, name='patient_list'),
    url(r'^patient/(?P<pk>V\d+)/$', views.patient_detail, name='patient_detail'),
    url(r'^patient/(?P<pk>V\d+)/edit/$', views.patient_edit, name='patient_edit'),    
    ]
