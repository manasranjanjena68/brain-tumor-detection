from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'timestamp')
    search_fields = ('user__username', 'question', 'answer')
    