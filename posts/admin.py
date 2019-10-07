from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'active', 'user')
    list_filter = ('active', 'created', 'user')
    search_fields = ('title', 'content')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    list_filter = ('created', 'user')
    search_fields = ('user', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
