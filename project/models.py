from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class project_detail(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, name="account")
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

fontawesome = [
    ('fa-regular fa-thumbs-up', 'thumbs-up'),
    ('fa-regular fa-heart', 'heart'),
    ('fa-regular fa-face-smile', 'face-smile'),
    ('fa-regular fa-face-grin-stars', 'face-grin-stars'),
    ('fa-regular fa-regular fa-face-grin-hearts', 'face-grin-hearts'),
    ('fa-regular fa-face-grin-beam', 'face-grin-beam'),
    ('', 'unselected')
]

class emoji(models.Model):
    fontawesome_classname = models.CharField(max_length=50, choices=fontawesome, default='')
    engagement = models.IntegerField(default = 0)
    account = models.ForeignKey(User, on_delete=models.CASCADE, name="account", default='')
    
    def __str__(self):
        return f"{self.fontawesome_classname}"