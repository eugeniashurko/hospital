from django.shortcuts import render
from django.views.generic import ListView, DetailView

import models


class PatientsView(ListView):
    model = models.Patient
    template_name = "histories/patients_history.html"
    context_object_name = "patients_list"