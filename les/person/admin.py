from django.contrib import admin

from .models import *


@admin.register(LocalityType)
class LocalityTypeAdmin(admin.ModelAdmin):
    list_display = ('locality_type', 'locality_type_sokr')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name', 'patronymic')


@admin.register(PersonPassport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('series', 'number')


@admin.register(PersonResidenceAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('locality', 'street', 'house_number', 'apartment_number')


@admin.register(RepresentativePassport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('series', 'number')


@admin.register(RepresentativeResidenceAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('locality', 'street', 'house_number', 'apartment_number')


@admin.register(RepresentativePerson)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name', 'patronymic')
