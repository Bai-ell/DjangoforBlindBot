from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Links, Contacts

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('ru_name', 'kg_name', 'link')
    search_fields = ('ru_name', 'kg_name', 'link')
    verbose_name = _("Link")
    verbose_name_plural = _("Links")

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('ru_name', 'kg_name', 'link')
    search_fields = ('ru_name', 'kg_name', 'link')
    verbose_name = _("Contact")
    verbose_name_plural = _("Contacts")
