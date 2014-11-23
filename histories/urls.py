from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    url(r'^$', views.PatientsView.as_view(), name="patients_view"),
)

