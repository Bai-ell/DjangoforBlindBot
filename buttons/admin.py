from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Buttons

@admin.register(Buttons)
class ButtonsAdmin(admin.ModelAdmin):
    list_display = ('pkname', 'button_ru', 'button_kg')
    list_filter = ('pkname',)
    search_fields = ('button_ru', 'button_kg')
    verbose_name = _("Button")
    verbose_name_plural = _("Buttons")
