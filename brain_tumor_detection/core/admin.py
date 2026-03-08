from django.contrib import admin
from django.utils.html import format_html
from .models import BrainTumorImage, PredictionHistory

@admin.register(BrainTumorImage)
class BrainTumorImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'preview')
    search_fields = ('id',)
    list_filter = ('uploaded_at',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No image"
    preview.short_description = 'Image Preview'


@admin.register(PredictionHistory)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'predicted_class', 'confidence', 'date', 'preview')
    search_fields = ('user__username', 'predicted_class')
    list_filter = ('date', 'predicted_class')

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No image"
    preview.short_description = 'MRI Image'
