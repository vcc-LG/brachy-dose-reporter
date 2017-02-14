from django.shortcuts import render

# Create your views here.
def patient_list(request):
    return render(request, 'doseapp/patient_list.html', {})
