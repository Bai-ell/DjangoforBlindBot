from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Mta, Institution

@admin.register(Mta)
class MtaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    verbose_name = _("MTA")
    verbose_name_plural = _("MTAs")

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('get_pkinstitutions_display', 'string_ru', 'string_kg')
    list_filter = ('pkinstitutions',)
    verbose_name = _("Institution")
    verbose_name_plural = _("Institutions")
