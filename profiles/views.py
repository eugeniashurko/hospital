from django.shortcuts import render
from django.views.generic import ListView, DetailView

import models


class DoctorProfileView(ListView):
    model = models.Doctor
    template_name = "profiles/doctor_main.html"
    context_object_name = "doctor_profile"


class NurseProfileView(ListView):
    model = models.Nurse
    template_name = "profiles/nurse_main.html"
    context_object_name = "nurse_profile"