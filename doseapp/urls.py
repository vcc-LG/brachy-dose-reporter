from django.conf.urls import url
from . import views
from .views import PatientList


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient/new/$', views.patient_new, name='patient_new'),
    url(r'^patient/new/fraction/$', views.fraction_new, name='fraction_new'),
    # url(r'^patient/list/$', views.patient_list, name='patient_list'),
    url(r'^patient/list/$',  PatientList.as_view(), name="patient_list"),
    url(r'^patient/(?P<pk>V\d+)/$', views.patient_detail, name='patient_detail'),
    url(r'^patient/(?P<pk>V\d+)/edit/$', views.patient_edit, name='patient_edit'),
    url(r'^fraction/(?P<pk>V\d+)/(?P<fraction_num>[0-9])/edit/$', views.fraction_edit, name='fraction_edit'),
    ]
