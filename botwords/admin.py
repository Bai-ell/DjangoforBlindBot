from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import BotWords

@admin.register(BotWords)
class BotWordsAdmin(admin.ModelAdmin):
    list_display = ('pkwords', 'botwords_ru', 'botwords_kg')
    list_filter = ('pkwords',)
    search_fields = ('botwords_ru', 'botwords_kg')
    verbose_name = _("Bot Word")
    verbose_name_plural = _("Bot Words")