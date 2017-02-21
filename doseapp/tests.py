from django.test import TestCase
from doseapp.models import Patient, Fraction

class IndexViewTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class ListViewTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/patient_list/')
        self.assertEqual(resp.status_code, 200)


class PatientDetailTestCase(TestCase):
    def test_index(self):
        test_patient_id = 'V666666'
        test_patient = Patient.objects.create(
            patient_id=test_patient_id,
            first_name='django',
            last_name='test')
        Patient.objects.filter(pk=test_patient.pk).update(first_name='dingo')
        test_patient.refresh_from_db()
        self.assertEqual(test_patient.first_name, 'dingo')
