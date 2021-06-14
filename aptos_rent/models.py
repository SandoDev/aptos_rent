from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from djmoney.models.fields import MoneyField
from . import constants


class Aptos(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    address = models.CharField(max_length=200)
    score_address = models.PositiveSmallIntegerField(
        choices=constants.SCORE_ADDRESS
    )
    phone = models.CharField(max_length=20)
    flat = models.PositiveSmallIntegerField(help_text="Número de piso")
    bedrooms = models.PositiveSmallIntegerField(
        help_text="Número de Habitaciones")
    toilets = models.PositiveSmallIntegerField(help_text="Número de baños")
    socre_kitchen = models.PositiveSmallIntegerField(
        choices=constants.SCORE_KITCHEN
    )
    score_dining_room = models.PositiveSmallIntegerField(
        choices=constants.SCORE_SIZE
    )
    score_backyard = models.PositiveSmallIntegerField(
        choices=constants.SCORE_SIZE
    )
    price = MoneyField(
        decimal_places=0,
        max_digits=8,
        default_currency="COP"
    )
    observations = models.TextField(null=True, blank=True)
    final_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + \
            self.created_at.__format__('%Y-%m-%d %H:%M') + ' - ' + \
            self.address


class Manage(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    manage_apto = models.OneToOneField(
        Aptos,
        on_delete=models.CASCADE,
        primary_key=True
    )
    status = models.CharField(
        max_length=11,
        choices=constants.STATUS_MANAGE,
        default='Not started'
    )
    description = models.TextField(null=True, blank=True)


@receiver(post_save, sender=Aptos)
def my_handler(sender, instance, **kwargs):
    Manage.objects.create(manage_apto=instance)
