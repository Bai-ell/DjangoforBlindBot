from django.db import models
from django.utils.translation import gettext_lazy as _

class Questionnaire(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    phone_number = models.CharField(max_length=20, verbose_name=_("Phone Number"))
    date_of_birth = models.CharField(max_length=25, verbose_name=_("Date of Birth"))
    microdistrict = models.TextField(verbose_name='Micro_District',default='')
    residentail_area = models.TextField(verbose_name='Residentail_are', default='')
    street = models.TextField(verbose_name='Street',default='')
    house_number = models.TextField(verbose_name='House_Number',default='')
    apartment_number = models.TextField(verbose_name='ApartmentNumber',default='')
    type_gift = models.CharField(max_length=255, verbose_name=_("Type of Gift"))
    text = models.TextField(verbose_name=_("Text"))
    checked = models.BooleanField(default=False, verbose_name=_("Checked"))

    class Meta:
        verbose_name = _("Questionnaire")
        verbose_name_plural = _("Questionnaires")

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.type_gift}"


class TypeGift(models.Model):
    gift_type_ru = models.CharField(max_length=255, default='non', verbose_name=_("Gift Type (RU)"))
    gift_type_kg = models.CharField(max_length=255, default='non', verbose_name=_("Gift Type (KG)"))

    class Meta:
        verbose_name = _("Type of Gift")
        verbose_name_plural = _("Types of Gift")

    def __str__(self):
        return f"RU: {self.gift_type_ru} | KG: {self.gift_type_kg}"