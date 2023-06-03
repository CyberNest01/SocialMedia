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


def blog_file(instance, filename):
    return "%s/%s/%s" % ('blog', instance.username, filename)


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=blog_file, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    is_comment = models.BooleanField(default=True)
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


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

