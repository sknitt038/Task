from rest_framework import serializers
from .models import CustomUser, ActivityPeriods

import datetime
import six
from rest_framework.utils import encoders


class JSONEncoder(encoders.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.tzinfo):
            return six.text_type(obj)
        return super(JSONEncoder, self).default(obj)


class CustomUserSerializer(serializers.ModelSerializer):
    timezone = serializers.SerializerMethodField()

    class Meta:
        """Map this serializer to a model and their fields."""
        model = CustomUser
        fields = ['username', 'real_name', 'timezone', 'last_login']
        depth = 2

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


class ActivityPeriodsSerializer(serializers.ModelSerializer):

    class Meta:
        """Map this serializer to a model and their fields."""
        model = ActivityPeriods
        fields = '__all__'
        depth=0

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


