from django.contrib import admin

from .models import Reference, Comment, Tag

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2

class TagInline(admin.StackedInline):
    model = Reference.tags.through
    extra = 2

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tag_name']})
    ]

class ReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {
                'fields': ['ref_name', 'author']
                }),
            ('File metadata', {
                'fields': ['url', 'filetype']
                }),
            ]
    inlines = [CommentInline, TagInline]


admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Tag, TagAdmin)
