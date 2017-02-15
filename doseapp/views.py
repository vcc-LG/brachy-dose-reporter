from django.shortcuts import render
from .models import Patient, Fraction
from .forms import PatientForm
from django.shortcuts import redirect

# Create your views here.
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'doseapp/patient_list.html',{'patients':patients})

def index(request):
    return render(request,'doseapp/index.html')

def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'doseapp/patient_new.html', {'form': form})
