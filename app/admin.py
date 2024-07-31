from django.contrib import admin
from app.models import *

# Register your models here.

class TagTabularInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTabularInline]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)