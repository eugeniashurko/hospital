from django.contrib import admin
from .models import Doctor, Nurse

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth', 'telephone', 'address')

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth', 'telephone', 'address')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
