from django.contrib import admin

from models import Department, Room


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','building', 'address')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'capacity')


# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Room, RoomAdmin)
