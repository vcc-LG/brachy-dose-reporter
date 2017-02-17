from django.shortcuts import render
from .models import Patient, Fraction
from .forms import PatientForm, FractionForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import UpdateView

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

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    # fractions =  get_object_or_404(Fraction, patient=pk)
    fractions = Fraction.objects.filter(patient=pk)
    # fractions =  get(Fraction, patient=pk)
    return render(request, 'doseapp/patient_detail.html', {'patient': patient, 'fractions':fractions})

def fraction_new(request):
    print(request.META.get('HTTP_REFERER'))
    referrer_id = request.META.get('HTTP_REFERER').rsplit('/',2)[1]
    if request.method == "POST":
        form = FractionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('patient_list')
    else:
        form = FractionForm()
    return render(request, 'doseapp/fraction_new.html', {'form': form, 'patient_id':referrer_id})


def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('patient_detail', pk=post.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'doseapp/patient_edit.html', {'form': form})

def fraction_edit(request, pk, fraction_num):
    fraction = get_object_or_404(Fraction, patient=pk, fraction_number=fraction_num)
    if request.method == "POST":
        form = FractionForm(request.POST, instance=fraction)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('patient_detail', pk=pk)
    else:
        form = FractionForm(instance=fraction)
    return render(request, 'doseapp/fraction_edit.html', {'form': form})
