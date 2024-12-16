from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)  
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_photo(self):
        return self.photo.url if self.photo else self.photo_url

    class Meta:
        ordering = ['-created_at']
