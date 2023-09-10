from django.contrib import admin

from posts.models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text', 'author__username', 'group__title')
    list_filter = ('pub_date', 'group')
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
