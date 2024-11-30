from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Questionnaire, TypeGift

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'date_of_birth', 'type_gift', 'checked')
    search_fields = ('name', 'phone_number', 'address', 'type_gift')
    list_filter = ('checked',)
    verbose_name = _("Questionnaire")
    verbose_name_plural = _("Questionnaires")

@admin.register(TypeGift)
class TypeGiftAdmin(admin.ModelAdmin):
    list_display = ('gift_type_ru', 'gift_type_kg')
    search_fields = ('gift_type_ru', 'gift_type_kg')
    verbose_name = _("Type of Gift")
    verbose_name_plural = _("Types of Gift")
