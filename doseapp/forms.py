from django import forms

from .models import Patient, Fraction

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('patient_id',
        'first_name',
        'last_name',)

class FractionForm(forms.ModelForm):

    class Meta:
        model = Fraction
        fields = ('fraction_number',
        'D90',)
