from django.contrib import admin

from messenger.models import UserMessage


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    pass

