from django.db import models

class Tag(models.Model):
    tags = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tags

class Author(models.Model):
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=50)
    email = models.EmailField()
    

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    image_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True , db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author , on_delete=models.SET_NULL , null=True , related_name="posts")
    tags = models.ManyToManyField(Tag)
    
    