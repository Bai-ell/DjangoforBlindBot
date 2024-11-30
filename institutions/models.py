from django.db import models
from django.utils.translation import gettext_lazy as _

class Mta(models.Model):
    string_ru = models.TextField(verbose_name=_("Russian Text"))
    string_kg = models.TextField(verbose_name=_("Kyrgyz Text"))

    class Meta:
        verbose_name = _("MTA")
        verbose_name_plural = _("MTAs")

    @classmethod
    def get_mta_by_id(cls, mta_id):
        try:
            return cls.objects.get(id=mta_id)
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return f"RU: {self.string_ru[:50]} | KG: {self.string_kg[:50]}"


class Institution(models.Model):
    class PkInstitutions(models.TextChoices):
        OOU = 'Oou', _('Oou')
        MED = 'Med', _('Med')

    string_ru = models.TextField(verbose_name=_("Russian Text"))
    string_kg = models.TextField(verbose_name=_("Kyrgyz Text"))
    pkinstitutions = models.CharField(
        max_length=255, 
        choices=PkInstitutions.choices, 
        default=PkInstitutions.OOU, 
        verbose_name=_("Institution Type")
    )

    class Meta:
        verbose_name = _("Institution")
        verbose_name_plural = _("Institutions")

    @classmethod
    def get_med_institution_by_id(cls, institution_id):
        try:
            return cls.objects.get(id=institution_id)
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return f"{self.get_pkinstitutions_display()} - RU: {self.string_ru[:50]} | KG: {self.string_kg[:50]}"
