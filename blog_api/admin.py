from django.contrib import admin

from blog_api.models import Post
from blog_api.models import Comment

admin.site.register(Post)
admin.site.register(Comment)