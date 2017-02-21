from django.shortcuts import render
from .models import Patient, Fraction
from .forms import PatientForm, FractionForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView


# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request, 'doseapp/patient_list.html',{'patients':patients})


class PatientList(TemplateView):
    template_name = 'doseapp/patient_list.html'

class PatientListJson(BaseDatatableView):
    model = Patient
    columns = ['patient_id', 'first_name', 'last_name']
    order_columns = ['patient_id', 'first_name', 'last_name']

    def render_column(self, row, column):
        if column == 'patient_id':
            return '<a href="%s">%s</a>' %('../patient/'+row.patient_id,row.patient_id)
        else:
            return super(PatientListJson, self).render_column(row, column)

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
    # print(request.META.get('HTTP_REFERER'))
    # print(request.META.get('HTTP_REFERER').rsplit('/',2)[1])
    referrer_id = request.META.get('HTTP_REFERER').rsplit('/',2)[1]
    if request.method == "POST":
        form = FractionForm(request.POST)
        #form.cleaned_data['patient'] = request.POST['patid']
        if form.is_valid():
            #form['patient'] = request.POST['patid']
            post = form.save(commit=False)
            # print(request.POST['patid'])
            post.save()
            return redirect('patient_detail', pk=post.patient_id)
    else:
        form = FractionForm(initial={"patient": referrer_id})
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
