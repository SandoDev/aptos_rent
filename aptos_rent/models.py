from django.db import models
from . import constants
from djmoney.models.fields import MoneyField


class Aptos(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    address = models.CharField(max_length=200)
    score_address = models.SmallIntegerField(
        choices=constants.SCORE_ADDRESS
    )
    phone = models.CharField(max_length=20)
    flat = models.SmallIntegerField(help_text="Número de piso")
    bedrooms = models.SmallIntegerField(help_text="Número de Habitaciones")
    toilets = models.SmallIntegerField(help_text="Número de baños")
    socre_kitchen = models.SmallIntegerField(
        choices=constants.SCORE_KITCHEN
    )
    score_dining_room = models.SmallIntegerField(
        choices=constants.SCORE_SIZE
    )
    score_backyard = models.SmallIntegerField(
        choices=constants.SCORE_SIZE
    )
    price = MoneyField(
        decimal_places=0,
        max_digits=8,
        default_currency="COP"
    )
    observations = models.TextField(null=True, blank=True)
    final_score = models.FloatField(null=True, blank=True)
