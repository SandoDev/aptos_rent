from django.contrib import admin
from .models import Aptos


@admin.register(Aptos)
class AptosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'created_at',
        'address',
        'score_address',
        'flat',
        'bedrooms',
        'socre_kitchen',
        'score_dining_room',
        'score_backyard',
        'price',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    ordering = ['-created_at']
    list_filter = [
        'status',
        'score_address',
        'flat',
        'bedrooms',
        'socre_kitchen',
        'score_dining_room',
        'score_backyard',
    ]
    search_fields = ['address', 'price']
