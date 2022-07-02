from django.db import models
from django.conf import settings

from PIL import Image

import os

from auth_api.models import User


def use_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/{1}.jpg'.format(instance.added_by.id, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to=use_directory_path, blank=True, null=True, verbose_name='Picture')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title) + ' - ' + str(self.added_by)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment) + ' - ' + str(self.added_by)