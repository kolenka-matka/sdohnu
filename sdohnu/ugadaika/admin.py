from django.contrib import admin
from .models import Styles, Artists, Genres, Techniques, Paintings


class PaintingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'style', 'artist']

# Register your models here.
admin.site.register(Styles)
admin.site.register(Artists)
admin.site.register(Paintings, PaintingsAdmin)
admin.site.register(Genres)
admin.site.register(Techniques)