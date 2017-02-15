from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient/new/$', views.patient_new, name='patient_new'),
    url(r'^patient/list/$', views.patient_list, name='patient_list'),
]
