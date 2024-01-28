from django.db import models


class Birthday(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Фамилия',
        help_text='Необязательное поле'
    )
    birthday = models.DateField(verbose_name='Дата рождения')
