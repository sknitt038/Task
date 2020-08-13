# Signals that fires when a user logs in and logs out

from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

from .models import LoggedInUser, ActivityPeriods, CustomUser


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    if kwargs.get('user'):
        data = CustomUser.objects.filter(username=kwargs.get('user')).all()
        print(timezone.now())
        data1 = ActivityPeriods(user_id=data[0].id, start_time=data[0].last_login,  end_time=timezone.now())
        data1.save()

    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
