from django.contrib import admin
from apps.empleados.models import Empleado, AgendaTelefonica
# Register your models here.


class AgendaTelefonicaInline(admin.TabularInline):
    model = AgendaTelefonica
    extra = 0


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', )
    search_fields = ('nombre', 'apellido')
    inlines = [AgendaTelefonicaInline]


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(AgendaTelefonica)
