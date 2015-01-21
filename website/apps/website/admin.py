from django.contrib import admin

from website.models import *


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id

        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'status', 'author', 'publish')
        }),

    )

admin.site.register(Post, PostAdmin)


class PoemAdmin(admin.ModelAdmin):

    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id

        return super(PoemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'status', 'author', 'publish')
        }),

    )
admin.site.register(Poem, PoemAdmin)


class LetterAdmin(admin.ModelAdmin):

    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id

        return super(LetterAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'status', 'author', 'publish')
        }),

    )
admin.site.register(Letter, LetterAdmin)
