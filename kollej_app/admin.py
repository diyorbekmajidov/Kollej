from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


admin.site.register(Petitions)

@admin.register(RegularlyQuestion)
class RegularlyQuestionAdmin(TranslationAdmin):
    list_display= ("question",)
@admin.register(Leadership)
class LeadershipAdmin(TranslationAdmin):
    list_display = ("full_name",)

@admin.register(DirectionsModel)
class DirectionsAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(OpenData)
class OpenDataAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(Requisites)
class RequisitesAdmin(TranslationAdmin):
    list_display = ('college_name',)
