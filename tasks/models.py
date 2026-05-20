from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
class Project (models.Model):
    name = models.CharField(max_length=100, verbose_name="Название проекта")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='managed_projects',
        limit_choices_to={'role': 'manager'},
        verbose_name="Менеджер проекта"
    )
    def __str__(self):
        return self.name
class Task(models.Model):
        STATUS_CHOICES = (
            ('new', 'Новая'),
            ('in_progress', 'В работе'),
            ('completed', 'Завершена'),
        )

        title = models.CharField(max_length=150, verbose_name="Заголовок задачи")
        description = models.TextField(blank=True, verbose_name="Описание")
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new',verbose_name="Статус")
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

        project = models.ForeignKey(
            Project,
            on_delete=models.CASCADE,
            related_name='tasks',
            verbose_name="Проект"
        )

        executor = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='tasks',
            limit_choices_to={'role': 'developer'},
            verbose_name="Исполнитель"
        )

        def __str__(self):
            return f"{self.title} ({self.get_status_display()})"