from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import re
from django.utils.html import mark_safe


@deconstructible
class _PhoneValidator:

    _pattern = re.compile(
        r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    )

    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError("{!r}You have entered an incorrect number.".format(value))


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        validators=[_PhoneValidator()],
        null=True,
        verbose_name="User",
    )

    def show_image(self):
        return mark_safe('<img src="{}" width="50px" />'.format(
            "https://www.softportal.com/scr/32691/matrix-screensaver-big-3.png"
            )
        )
    show_image.short_decription = "Matrix"
    show_image.allow_tags = True
    

    def __str__(self):
        return self.username

    
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"




 





