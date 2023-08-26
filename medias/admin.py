from django.contrib import admin
from medias.models import Category, Media

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["name"]

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    readonly_fields = ["number_of_views", "rating"]
    list_display = ["id", "name"]
    fields = ["name", "categories", "type", "number_of_views", "rating"]

    def number_of_views(self, obj):
        return obj.number_of_views
    number_of_views.short_description = 'Número de vistas'

    def rating(self, obj):
        return obj.rating
    rating.short_description = 'Puntaje promedio'