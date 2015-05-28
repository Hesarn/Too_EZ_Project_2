from django.contrib import admin
from .models import MyUser, Post, Cast, Comment, Film

admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Cast)
admin.site.register(Comment)
admin.site.register(Film)
