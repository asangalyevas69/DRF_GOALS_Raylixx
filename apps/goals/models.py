from django.db import models
from django.contrib.auth.models import User

from core import settings


class Goal(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @property
    def progress(self) -> int:
        steps = self.steps.all()
        if not steps.exists():
            return 0
        completed = steps.filter(is_done=True).count()
        return int((completed / steps.count()) * 100)


class Step(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

