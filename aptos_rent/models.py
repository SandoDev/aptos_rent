from django.db import models
from . import constants
# Create your models here.


class Aptos(models.Model):
    address = models.CharField(max_length=200)
    score_address = models.SmallIntegerField(
        choices=constants.SCORE_ADDRESS
    )
