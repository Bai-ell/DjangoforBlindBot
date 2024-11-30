from django.db import models
from django.utils.translation import gettext_lazy as _

class Links(models.Model):
    ru_name = models.CharField(max_length=50, verbose_name=_("Russian Name"))
    kg_name = models.CharField(max_length=50, verbose_name=_("Kyrgyz Name"))
    link = models.CharField(max_length=255, verbose_name=_("Link"))

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return f"{self.ru_name} ({self.link})"


class Contacts(models.Model):
    ru_name = models.CharField(max_length=50, verbose_name=_("Russian Name"))
    kg_name = models.CharField(max_length=50, verbose_name=_("Kyrgyz Name"))
    link = models.CharField(max_length=255, verbose_name=_("Link"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f"{self.ru_name} ({self.link})"
