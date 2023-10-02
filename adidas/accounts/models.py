from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.TextField(max_length=200, verbose_name="Имя", blank=True, null=True)
    last_name = models.TextField(max_length=200, verbose_name="Фамилия", blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    email = models.EmailField(max_length=300, verbose_name="Email", blank=True, null=True)

    def __str__(self):
        return f"{self.pk} {self.first_name} {self.last_name} {self.phone} {self.email}"

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
