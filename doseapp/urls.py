from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.patient_list, name='patient_list'),
]
