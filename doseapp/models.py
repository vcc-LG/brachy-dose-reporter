from django.db import models
from django.utils import timezone
from django_datatables_view.base_datatable_view import BaseDatatableView


class Patient(models.Model):
    """
    A class to hold the patient model.
    """
    patient_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.patient_id


class Fraction(models.Model):
    """
    A class to hold the fraction details.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fraction_number = models.IntegerField(blank=False)
    D90 = models.FloatField(blank=False)
