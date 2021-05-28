from django.contrib import admin
from .models import Aptos

# admin.site.register(Aptos)


@admin.register(Aptos)
class AptosAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'score_address',
        'flat',
        'bedrooms',
        'toilets',
        'socre_kitchen',
        'score_dining_room',
        'score_backyard',
        'price',
        'final_score'
    )
    readonly_fields = [
        'created_at',
    ]
