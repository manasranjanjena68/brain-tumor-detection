from django.db import models
from django.contrib.auth.models import User

class BrainTumorImage(models.Model):
    image = models.ImageField(upload_to='brain_tumor_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.uploaded_at.strftime('%Y-%m-%d')}"

    # ✅ Image preview for admin
    def image_tag(self):
        if self.image:
            return f'<img src="{self.image.url}" width="100"/>'
        return "No Image"
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True


class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='history_images/')
    predicted_class = models.CharField(max_length=100)
    confidence = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_class} - {self.date.strftime('%Y-%m-%d')}"

    # ✅ Image preview for admin
    def image_tag(self):
        if self.image:
            return f'<img src="{self.image.url}" width="100"/>'
        return "No Image"
    image_tag.short_description = 'MRI Image'
    image_tag.allow_tags = True
