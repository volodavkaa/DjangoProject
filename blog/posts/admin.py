from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'photo_url_display')
    prepopulated_fields = {'slug': ('title',)}

    def photo_url_display(self, obj):
        return obj.get_photo() if obj.get_photo() else "Фото відсутнє"

    photo_url_display.short_description = "Фото"
