from django.conf.global_settings import  AUTH_USER_MODEL
from django.db import models

class UserMessage(models.Model):
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.sender} - {self.receiver} : {self.message}'



