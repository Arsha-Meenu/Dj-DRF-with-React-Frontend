from django.db import models
from apps.users.models import CustomUser as User

class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)
    published = models.DateTimeField(auto_now_add=True)
    article_author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return  self.title