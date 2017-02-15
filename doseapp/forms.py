from django import forms

from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('patient_id',
        'first_name',
        'last_name',)
