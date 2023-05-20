from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


def profile_image(instance, filename):
    return "%s/%s/%s" % ('profile', instance.username, filename)


class User(AbstractUser):
    cellphone = models.CharField(max_length=255, null=True, blank=True)
    privet = models.BooleanField(default=False)
    age = models.DateTimeField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=profile_image, null=True, blank=True)
    report_count = models.IntegerField(default=0)
    ban = models.BooleanField(default=False)

    def login(self, request):
        if self.is_active:
            login(request, self)
            return True
        return False

    def ban_user(self):
        self.ban = True
        self.save()

    def ban_user_count(self):
        if self.report_count == 10:
            self.ban_user()
        else:
            return 0


class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="report_owner")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="report_user")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def report_user(self):
        self.user.report_count += 1
        self.user.save()


class Friends(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends_owner")
    users = models.ManyToManyField(User, related_name="friends_users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
