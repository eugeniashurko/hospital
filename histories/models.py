from django.db import models
from django.utils.translation import ugettext_lazy as _

from profiles.models import Doctor



class Patient(models.Model):
    name = models.CharField(_(u'Name'), max_length=255)
    date_of_birth = models.DateField(_(u'Date of birth'), blank=True, null=True)
    telephone = models.CharField(_(u'Telephone'), max_length=255, blank=True, null=True)
    address = models.CharField(_(u'Address'), max_length=255, blank=True, null=True)
    occupation = models.CharField(_(u'Occupation'), max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class MedicalCard(models.Model):
    date_issued = models.DateField(_(u'Date Issued'), blank=True, null=True)
    patient = models.ForeignKey(Patient)

    class Meta:
        verbose_name = _('Medical Card')
        verbose_name_plural = _('Medical Cards')
        ordering = ('date_issued',)

    def __unicode__(self):
        return (str(self.date_issued) + ' ' + self.patient.__unicode__())


class MedicalHistory(models.Model):
    medical_card = models.OneToOneField(MedicalCard);
    preliminary_diagnosis = models.CharField(_(u'Preliminary Diagnosis'), max_length=255)
    start_date = models.DateField(_(u'Start Date'))
    end_date = models.DateField(_(u'End Date'), blank=True, null=True)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, related_name="Medical History", \
        related_query_name="Medical History")
    complaints = models.TextField(_(u'Complaints'))
    anamnesis = models.TextField(_(u'Anamnesis'), blank=True, null=True)
    objective_examination = models.TextField(_(u'Objective Examination'), blank=True, null=True)
    final_diagnosis = models.CharField(_(u'Final Diagnosis'), max_length=255, blank=True, null=True)
    associated_disease = models.CharField(_(u'Associated Disease'), max_length=255, blank=True, null=True)
    complications = models.TextField(_(u'Complications'), blank=True, null=True)
    treatment_plan = models.TextField(_(u'Treatment Plan'), blank=True, null=True)

    class Meta:
        verbose_name = _('Medical History')
        verbose_name_plural = _('Medical Histories')
        ordering = ('start_date',)

    def __unicode__(self):
        return (self.medical_card.__unicode__() + ' ' + self.preliminary_diagnosis)


class LaboratoryTest(models.Model):
    medical_history = models.OneToOneField(MedicalHistory)
    name = models.CharField(_(u'Name'), max_length=255)
    date_taken = models.DateField(_(u'Date Taken'))
    place_taken = models.CharField(_(u'Place Taken'), max_length=255)
    date_measured = models.DateField(_(u'Date Measured'))
    results = models.TextField(_(u'Results'))

    def __unicode__(self):
        return (self.medical_history.__unicode__() + ' ' + self.name)