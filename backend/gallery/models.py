from django.db import models
from django.utils import timezone
import os

def gallery_upload_path(instance, filename):
    """
    Custom upload path for gallery images.
    Format: gallery/year/month/day/filename
    """
    date = timezone.now().strftime('%Y/%m/%d')
    return f'gallery/{date}/{filename}'

class GalleryImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=gallery_upload_path)
    caption = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title or f"Image {self.pk}"
    
    def filename(self):
        return os.path.basename(self.image.name)
    
    def image_url(self):
        if self.image:
            return self.image.url
        return None
