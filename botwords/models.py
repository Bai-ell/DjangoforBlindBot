from django.db import models
from django.utils.translation import gettext_lazy as _

class BotWords(models.Model):
    class PkNames(models.TextChoices):
        GREETINGS = 'Greetings', _('Greetings')
        CHANGELANG = 'ChangeLang', _('ChangeLang')
        INFOOCTOBERAREA = 'InfoOctoberArea', _('InfoOctoberArea')
        MTB = 'Mtb', _('Mtb')
        MED = 'Med', _('Med')
        OOU = 'OOU', _('OOU')
        CONNECT = 'Connect', _('Connect')
        LINKS = 'Links', _('Links')
        CONTACTS = 'Contacts', _('Contacts')
        CHOICE = 'Choice', _('Choice')
        GOTOMENU = 'GoToMenu', _('GoToMenu')
        CHOICEGIFT = 'ChoiceGift', _('ChoiceGift')
        QUESTIONNAIRE = 'Questionnaire', _('Questionnaire')
        STARTQUESTIONNAIRE = 'StartQuestionnaire', _('StartQuestionnaire')
        CHOICEGIFTQUESTIONNAIRE = 'ChoiceGiftQuestionnaire', _('ChoiceGiftQuestionnaire')
        ANSWERNAME = 'AnswerName', _('AnswerName')
        ANSWERPHONENUMBER = 'AnswerPhoneNumber', _('AnswerPhoneNumber')
        ANSWERDATEOFBIRTH = 'AnswerDateOfBirth', _('AnswerDateOfBirth')
        ANSWERADRESS = 'AnswerAdress', _('AnswerAdress')
        ENDQUESTIONNAIRE = 'EndQuestionnaire', _('EndQuestionnaire')
        GIFT = 'Gift', _('Gift')
        NAME = 'Name', _('Name')
        PHONE = 'Phone', _('Phone')
        BIRTHDATE = 'BirthDate', _('BirthDate')
        ADDRESS = 'Address', _('Address')
        SENDQUESTIONNAIRE = 'SendQuestionnaire', _('SendQuestionnaire')
        WARNINGWORD = 'WarningWord', _('WarningWord')
        DATASEND = 'DataSend', _('DataSend')
        CORRECTNUMBER = 'CorrectNumber', _('CorrectNumber')
        CORRECTDATE = 'CorrectDate', _('CorrectDate')
        ADDITIONALREQUEST = 'AdditionalInfoRequest', _('AdditionalInfoRequest')
        ADDITONALTEXT = 'AdditionalText', _('AdditionalText')
        ANSWERDISTRICT = 'AnswerDistrict', _('AnswerDistrict')
        ANSWERSTREET = 'AnswerStreet', _('AnswerStreet')
        ANSWERAPARTMENTNUMBER = 'AnswerApartmentNumber', _('AnswerApartmentNumber')
        ANSWERHOUSENUMBER = 'AnswerHouseNumber', _('AnswerHouseNumber')
        DISTRICT = 'District', _('District')
        STREET = 'Street', _('Street')
        HOUSENUMBER = 'HouseNumber', _('HouseNumber')
        APARTMENTNUMBER =  'ApartmentNumber', _('ApartmentNumber')
        DEFAULTSTREETWORD = 'DefaultStreetWord', _('DefaultStreetWord')
        IFNOTINFO = 'IfNotInfo', _('IfNotInfo')
        DEFAULTADDITIONALINFO = 'DefaultAdditionalInfo', _('DefaultAdditionalInfo')
        DEFAULTDISTRICT = 'Defaultdistrict', _('Defaultdistrict')
        DEFAULTRESIDENTAILAREA = 'DefaultResidentailArea', _('DefaultResidentailArea')
        DEFAULTDISTRICTWORD = 'DefaultDistrictWord', _('DefaultDistrictWord')
        DEFAULTRESIDENTAILAREAWORD  = 'DefaultResidentailAreaWord', _('DefaultResidentailAreaWord')
        CHOICERESIDENTAILAREA = 'ChoiceResidentailArea', _('ChoiceResidentailArea')
        CHOICEMICRODISTRICT = 'ChoiceMicrodistrict', _('ChoiceMicroDistrict')
        ANSWERRESIDENTAILAREA  = 'AnswerResidentailArea', _('AnswerResidentailArea')
        ANSWERMICRODISTRICT  = 'AnswerMicrodistrict', _('AnswerMicroDistrict')
        




    botwords_ru = models.TextField(verbose_name=_("Russian Text"))
    botwords_kg = models.TextField(verbose_name=_("Kyrgyz Text"))
    pkwords = models.CharField(max_length=255, choices=PkNames.choices, default=PkNames.GREETINGS, verbose_name=_("Keyword"))

    class Meta:
        verbose_name = _("Bot Word")
        verbose_name_plural = _("Bot Words")

    @classmethod
    def get_botwords_by_id(cls, botwords_id):
        try:
            return cls.objects.get(id=botwords_id)
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return f"{self.get_pkwords_display()} - RU: {self.botwords_ru[:50]} | KG: {self.botwords_kg[:50]}"
