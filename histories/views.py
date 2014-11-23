from django.shortcuts import render
from django.views.generic import ListView, DetailView

import models


class PatientsView(ListView):
    model = models.Patient
    template_name = "histories/patients_history.html"
    context_object_name = "patients_list"


class PrescriptionsView(ListView):
    model = models.Prescription
    template_name = "histories/prescription.html"
    context_object_name = "prescription_list"

class MedicalHistoryView(DetailView):
    def get_object(self):
        print self.kwargs['slug']
        return self.kwargs['slug']

    model = models.MedicalHistory
    slug_field = "medicalhistory"
    template_name = "histories/history_details.html"
    context_object_name = "history_details"
