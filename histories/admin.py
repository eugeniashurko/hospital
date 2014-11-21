from django.contrib import admin

from .models import Patient, MedicalHistory, MedicalCard, LaboratoryTest


class MedicalCardInline(admin.StackedInline):
    model = MedicalCard
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth', 'telephone', 'occupation')
    index_together = [
        ["name", "date_of_birth"],
    ]
    inlines=[MedicalCardInline]

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('preliminary_diagnosis', 'start_date', 'doctor')

class LaboratoryTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_taken', 'place_taken')

# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(LaboratoryTest, LaboratoryTestAdmin)

