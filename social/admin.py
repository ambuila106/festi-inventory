from django.contrib import admin
from social.models import Viewer, ViewerMedia

@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    fields = ["user"]

@admin.register(ViewerMedia)
class ViewerMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "media"]
    fields = ["viewer", "media", "rating", "has_watched"]