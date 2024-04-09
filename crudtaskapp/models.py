from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=20)
    description = models.TextField(100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title
