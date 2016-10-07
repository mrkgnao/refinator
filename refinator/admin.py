from django.contrib import admin

from .models import Reference, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2

class ReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {
                'fields': ['ref_name', 'author']
                }),
            ('File metadata', {
                'fields': ['url', 'filetype', 'size']
                }),
            ]
    inlines = [CommentInline]

admin.site.register(Reference, ReferenceAdmin)
