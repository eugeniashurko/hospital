from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    url(r'^$', views.PatientsView.as_view(), name="patients_view"),
    url(r'^(?P<slug>[\w+\-\.\_]+)/$', views.MedicalHistoryView.as_view(), name="medical_history_view"),
    url(r'^prescriptions', views.PrescriptionsView.as_view(), name="prescriptions_view")
)


