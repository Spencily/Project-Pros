from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class project_detail(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, name="project_details")
    title = models.CharField(max_length=120)
    # featured_image = CloudinaryField('image', default='placeholder')
    summary = models.CharField(max_length=500)
    collaborators = models.CharField(max_length=120)
    deployed_site = models.CharField(max_length=2048)
    github_repo = models.CharField(max_length=2048)
    reflections = models.TextField()
    approved = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-date_added"]
    
    def __str__(self):
        return f"{self.title}"


class emoji(models.Model):
    name = models.CharField(max_length=60)
    # emoji_image = CloudinaryField('image', default='placeholder')
    engagement = models.IntegerField(default = 0)
    project = models.ForeignKey(project_detail, on_delete=models.CASCADE, name="emojis")
    
    def __str__(self):
        return f"{self.name}"