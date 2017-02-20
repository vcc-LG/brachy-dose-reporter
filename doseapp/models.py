from django.db import models
from django.utils import timezone
from django_datatables_view.base_datatable_view import BaseDatatableView


class Patient(models.Model):
    patient_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.patient_id

class Fraction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fraction_number = models.IntegerField(blank=False)
    D90 = models.FloatField(blank=False)

    class OrderListJson(BaseDatatableView):
        # The model we're going to show
        model = Patient

        # define the columns that will be returned
        columns = ['patient_id', 'first_name', 'last_name']

        # define column names that will be used in sorting
        # order is important and should be same as order of columns
        # displayed by datatables. For non sortable columns use empty
        # value like ''
        order_columns = ['patient_id', 'first_name', 'last_name']

        # set max limit of records returned, this is used to protect our site if someone tries to attack our site
        # and make it return huge amount of data
        max_display_length = 500

        def filter_queryset(self, qs):
            # use parameters passed in GET request to filter queryset

            # simple example:
            search = self.request.GET.get(u'search[value]', None)
            if search:
                qs = qs.filter(name__istartswith=search)

            # # more advanced example using extra parameters
            # filter_customer = self.request.GET.get(u'customer', None)
            #
            # if filter_customer:
            #     customer_parts = filter_customer.split(' ')
            #     qs_params = None
            #     for part in customer_parts:
            #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
            #         qs_params = qs_params | q if qs_params else q
            #     qs = qs.filter(qs_params)
            return qs
