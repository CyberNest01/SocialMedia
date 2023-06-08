from datetime import datetime, timedelta

from django.db import models

from client.models import User, Friends


# Create your models here.


def story_file(instance, filename):
    return "%s/%s/%s" % ('story', instance.username, filename)


class Story(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_story')
    friends = models.ManyToManyField(User)
    privet = models.BooleanField(default=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    story_file = models.FileField(upload_to=story_file, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Story, self).save()

    def auto_delete(self):
        time = self.created_at + timedelta(hours=24)
        if datetime.now() > time:
            self.deleted = True
            self.save()


