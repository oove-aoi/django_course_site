from django.contrib import admin
from .models import Post,Comment, IpAddress

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "poster"]

class CommentAdmin(admin.ModelAdmin):
	list_display = ["user", "post"]

class IpAddressAdmin(admin.ModelAdmin):
	list_display = ['ip']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(IpAddress, IpAddressAdmin)