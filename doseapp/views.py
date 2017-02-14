from django.shortcuts import render
from .models import Patient, Fraction


# Create your views here.
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'doseapp/patient_list.html',{'patients':patients})
