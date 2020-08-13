from django.contrib import admin
from .models import CustomUser, ActivityPeriods

admin.site.register(CustomUser)
admin.site.register(ActivityPeriods)

#
# from django.contrib import admin
# from django.contrib.postgres import fields
# from django_json_widget.widgets import JSONEditorWidget
#
#
#
# @admin.register(CustomUser)
# class YourModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }