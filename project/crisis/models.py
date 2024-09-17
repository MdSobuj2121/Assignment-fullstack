from django.db import models

class Crisis(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='crisis_images/', null=True, blank=True)
    required_help = models.TextField()

    def __str__(self):
        return self.title
