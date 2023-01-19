from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "message",
        "message_length",
        "is_public",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["message"]
    list_filter = ["created_at", "is_public"]
    search_fields = ["message"]
