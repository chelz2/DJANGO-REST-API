from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
