from django.db import models
from django.urls import reverse


class AddTask(models.Model):
    title = models.CharField(max_length=278)
    description = models.TextField()
    image = models.ImageField(null = True, blank= True, upload_to = 'photos/blog')
    priority = models.PositiveIntegerField(choices=((1,"Low"),(2,"Medium"), (3,"High")))
    is_complete = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"{self.title}" 
    
    def get_absolute_url(self):
        return reverse('task')

