from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Scripture)
admin.site.register(quote)
admin.site.register(Notes)
admin.site.register(Post)
admin.site.register(AllSongs)
admin.site.register(Whatusay)
admin.site.register(Pics_day)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)