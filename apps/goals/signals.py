from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Goal
from .tasks import send_goal_done_email


@receiver(pre_save, sender=Goal)
def goal_status_change_handler(sender, instance, **kwargs):
    if not instance.pk:
        return

    previous = Goal.objects.get(pk=instance.pk)
    if previous.status != 'done' and instance.status == 'done':
        send_goal_done_email.delay(instance.user.id, instance.title)
