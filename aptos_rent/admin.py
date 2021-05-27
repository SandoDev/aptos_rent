from django.contrib import admin
from .models import Aptos


@admin.register(Aptos)
class AptosAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'score_address',
    )
