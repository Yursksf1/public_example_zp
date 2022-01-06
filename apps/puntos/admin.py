from django.contrib import admin
from apps.puntos.models import Punto, AgendaTelefonica


# Register your models here.
class AgendaTelefonicaInline(admin.TabularInline):
    model = AgendaTelefonica
    extra = 0


class PuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    inlines = [AgendaTelefonicaInline]

class AgendaTelefonicaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'punto')
    search_fields = ('numero', 'tipo', )
    list_filter = ('tipo',)


admin.site.register(Punto, PuntoAdmin)
admin.site.register(AgendaTelefonica, AgendaTelefonicaAdmin)
