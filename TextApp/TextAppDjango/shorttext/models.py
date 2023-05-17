from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Snippet(models.Model):
    text = models.CharField(max_length=255, null=False, blank=True, default='ShortText')
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, on_delete= models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    
    class Meta:
        ordering = ['created_at']
    