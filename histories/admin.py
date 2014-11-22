from django.contrib import admin

from .models import Patient, MedicalHistory, MedicalCard, LaboratoryTest, Record, \
                    Prescription


class MedicalCardInline(admin.StackedInline):
    model = MedicalCard
    extra = 1

class MedicalHistoryInline(admin.StackedInline):
    model = MedicalHistory
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth', 'telephone', 'occupation')
    index_together = [
        ["name", "date_of_birth"],
    ]
    inlines = [MedicalCardInline]

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('preliminary_diagnosis', 'start_date', 'doctor')

class LaboratoryTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_taken', 'place_taken')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('room',)
    inlines = [MedicalHistoryInline]

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'doctor', 'medical_history')

# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(LaboratoryTest, LaboratoryTestAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
