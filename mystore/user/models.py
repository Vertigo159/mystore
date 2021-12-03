from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import re


@deconstructible
class _PhoneValidator:

    _pattern = re.compile(
        "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    )

    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError("{!r} Некорректный телефонный номер.".format(value))


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        validators=[_PhoneValidator()],
        null=True,
        verbose_name="Номер телефона",
    )
    

    

    def __str__(self):
        return self.username

    
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"




 





