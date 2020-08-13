import pytz
from django.conf import settings
from django.db import models
from timezone_field import TimeZoneField
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, real_name, password):
        user = self.model(username=username, real_name=real_name, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, real_name, password):
        user = self.create_user(username=username, real_name=real_name, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        print(username_)
        return self.get(username=username_)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Here we are subclassing the Django AbstractBaseUser, which comes with only
    3 fields:
    1 - password
    2 - last_login
    3 - is_active
    Note than all fields would be required unless specified otherwise, with
    `required=False` in the parentheses.

    The PermissionsMixin is a model that helps you implement permission settings
    as-is or modified to your requirements.
    """
    username = models.CharField(max_length=20, unique=True)
    real_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    timezone = TimeZoneField(default='UTC', choices=[(tz, tz) for tz in pytz.all_timezones])
    REQUIRED_FIELDS = ['real_name']
    USERNAME_FIELD = 'username'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.username

    def natural_key(self):
        return self.username

    # Model to store the list of logged in users


class LoggedInUser(models.Model):
    user = models.OneToOneField(CustomUser, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    set = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


'''
@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        LoggedInUser.objects.create(customuser=instance)
        instance.customuser.save()

    def __str__(self):
        return self.username
'''


class ActivityPeriods(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='activity_periods_custom_user', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.user.username


