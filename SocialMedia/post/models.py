from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from client.models import User


# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def like_post(self):
        if not self.like:
            self.like = True
            self.save()

    def dislike_post(self):
        if self.like:
            self.like = False
            self.save()


def blog_file(instance, filename):
    return "%s/%s/%s" % ('blog', instance.username, filename)


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=blog_file, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    like = models.OneToOneField(Like, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Blog, self).save()


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Comments, self).save()


