from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Создаем кортеж с ролями. Первая строка — это код для БД, вторая — понятное человеку имя.
    ROLE_CHOICES = (
        ('manager', 'Менеджер'),
        ('developer', 'Разработчик'),
    )

    # Добавляем новое поле роли к стандартному пользователю
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='developer',
        verbose_name="Роль"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"