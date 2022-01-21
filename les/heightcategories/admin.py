from django.contrib import admin

from .models import *


@admin.register(Fff)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('diametrs',)
