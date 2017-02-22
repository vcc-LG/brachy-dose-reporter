from django import forms
from .models import Patient, Fraction


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id',
        'first_name',
        'last_name',)

class PatientImportForm(forms.Form):
    patient_id_to_lookup = forms.CharField(label=("Patient ID"),
        max_length=8,
        widget=forms.TextInput,
    )

class FractionForm(forms.ModelForm):
    class Meta:
        model = Fraction
        fields = ('patient',
        'fraction_number',
        'D90',)
        widgets = {'patient': forms.HiddenInput()} #this is so I can pass the patient ID
                                                   #between the patient detail view and
                                                   #the new fraction form... not ideal?
