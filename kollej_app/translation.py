from modeltranslation.translator import register, TranslationOptions
from .models import Leadership, DirectionsModel, OpenData,News, Requisites, RegularlyQuestion

@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = ('full_name', 'acceptions', 'position','adress',)

@register(DirectionsModel)
class DirectionsModelTranslationOptions(TranslationOptions):
    fields = ('name','body',)

@register(OpenData)
class OpenDataTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('body','title')

@register(Requisites)
class RequisitesTranslationOptions(TranslationOptions):
    fields = ('college_name','address')

@register(RegularlyQuestion)
class RegularlyQuestionTranslationOptions(TranslationOptions):
    fields = ('question','answer')