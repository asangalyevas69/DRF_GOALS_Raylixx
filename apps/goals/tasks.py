from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task
def send_goal_done_email(user_id: int, goal_title: str) -> None:
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            subject=f'🎯 Цель завершена: {goal_title}',
            message=f'Поздравляем! Ваша цель "{goal_title}" была завершена.',
            from_email='noreply@example.com',
            recipient_list=[user.email],
            fail_silently=False
        )
    except User.DoesNotExist:
        pass
