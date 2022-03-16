from django.contrib import admin

from .models import *


@admin.register(Diameter)
class DiameterAdmin(admin.ModelAdmin):
    list_display = ('name',)
