from django.contrib import admin
from .models import Aptos
from .models import Manage

# admin.site.register(Aptos)


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
    ]
    ordering = ['-created_at']
    list_filter = [
        'score_address',
        'flat',
        'bedrooms',
        'socre_kitchen',
        'score_dining_room',
        'score_backyard',
    ]
    search_fields = ['address', 'price']


@admin.register(Manage)
class ManageAdmin(admin.ModelAdmin):
    list_display = [
        'updated_at',
        'manage_apto',
        'status',
        'description',
    ]
    readonly_fields = [
        'updated_at',
    ]
    ordering = ['-updated_at']
    list_filter = [
        'status',
    ]
    search_fields = [
        'manage_apto__address',
        'manage_apto__price',
        'status',
        'description',
    ]
