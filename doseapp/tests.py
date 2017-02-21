from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class ListViewTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/patient_list/')
        self.assertEqual(resp.status_code, 200)


class ListViewTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/patient_list/')
        self.assertEqual(resp.status_code, 200)
