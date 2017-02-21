"""
View module for brachytherapy dose reporting app
"""

from django.shortcuts import render
from .models import Patient, Fraction
from .forms import PatientForm, FractionForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView


class PatientList(TemplateView):
    """
    Patient list class-based view.
    """
    template_name = 'doseapp/patient_list.html'


class PatientListJson(BaseDatatableView):
    """
    Returns a list of patients in JSON for insertion
    into the PatientList view
    """
    model = Patient
    columns = ['patient_id', 'first_name', 'last_name']
    order_columns = ['patient_id', 'first_name', 'last_name']

    def render_column(self, row, column):
        """
        Returns a list of patients in JSON for insertion
        into the PatientList view
        """
        if column == 'patient_id':
            return '<a href="%s">%s</a>' %('../patient/'+row.patient_id,
                                           row.patient_id)
        else:
            return super(PatientListJson, self).render_column(row, column)

def index(request):
    """
    Renders home page
    """
    return render(request, 'doseapp/index.html')

def patient_new(request):
    """
    View to hold new patient form
    """
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
    """
    View to display patient details (name, ID, fractions)
    """
    patient = get_object_or_404(Patient, pk=pk)
    fractions = Fraction.objects.filter(patient=pk)
    return render(request, 'doseapp/patient_detail.html',
                  {'patient': patient, 'fractions':fractions})

def fraction_new(request):
    """
    View to display new fraction form
    """
    referrer_id = request.META.get('HTTP_REFERER').rsplit('/', 2)[1]
    if request.method == "POST":
        form = FractionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('patient_detail', pk=post.patient_id)
    else:
        form = FractionForm(initial={"patient": referrer_id})
    return render(request, 'doseapp/fraction_new.html', {'form': form, 'patient_id':referrer_id})

def patient_edit(request, pk):
    """
    View to show new patient form but which will overwrite existing patient data
    """
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
    """
    Edit a fraction
    """
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
