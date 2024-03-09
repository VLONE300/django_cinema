from django.contrib import admin
from django.utils.safestring import mark_safe

from cinema.models import Actor, Movie, Genre, Director, Ticket, Show


class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_image')
    search_fields = ('first_name', 'last_name')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_image')
    search_fields = ('first_name', 'last_name')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'get_image')
    search_fields = ('title',)
    list_filter = ('genre',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')


class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'date', 'available_seats')
    search_fields = ('movie',)


admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)

admin.site.register(Ticket)
admin.site.register(Genre)
