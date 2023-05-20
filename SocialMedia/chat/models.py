from django.db import models
from client.models import User


# Create your models here.


class Chats(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats_owner")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats_user")
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Chats, self).save()


class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group_owner")
    users = models.ManyToManyField(User, related_name="group_users")
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    bio = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Group, self).save()


class Message(models.Model):
    chats = models.ForeignKey(Chats, on_delete=models.CASCADE, null=True, blank=True, related_name="message_chats")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name="message_group")
    text = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Message, self).save()

