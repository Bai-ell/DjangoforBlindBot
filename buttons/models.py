from django.db import models
from django.utils.translation import gettext_lazy as _

class Buttons(models.Model):
    class PkNames(models.TextChoices):
        BACK = 'Back', _('Back')
        CONNECT = 'Connect', _('Connect')
        AREAINFO = 'AreaInfo', _('AreaInfo')
        GIFT = 'Gift', _('Gift')
        CHOICEMENU = 'ChoiceMenu', _('ChoiceMenu')
        CHOICELANG = 'ChoiceLang', _('ChoiceLang')
        MENU = 'Menu', _('Menu')
        YES = 'Yes', _('Yes')
        NO = 'No', _('No')
        GOTOMENU = 'GoToMenu', _('GoTuMenu')
        NOAGAIN = 'NoAgain', _('NoAgain')
        SKIP = 'Skip', _('Skip')
        RESIDENTAILAREA = 'ResidentailArea', _('ResidentailArea')
        MICRODISTRICT = 'Microdistrict', _('Microdistrict')

    button_kg = models.CharField(max_length=255, verbose_name=_("Kyrgyz Button"))
    button_ru = models.CharField(max_length=255, verbose_name=_("Russian Button"))
    pkname = models.CharField(
        max_length=255, 
        choices=PkNames.choices, 
        default=PkNames.BACK, 
        verbose_name=_("Button Type")
    )

    class Meta:
        verbose_name = _("Button")
        verbose_name_plural = _("Buttons")

    @classmethod
    def get_button_by_id(cls, button_id):
        try:
            return cls.objects.get(id=button_id)
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return f"{self.get_pkname_display()} - RU: {self.button_ru} | KG: {self.button_kg}"
