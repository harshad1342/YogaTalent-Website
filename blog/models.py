from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.CharField(max_length=150)
    steps= models.TextField()
    benefit = models.TextField()
    image = models.ImageField(blank = True)
    image1 = models.ImageField(blank = True)
    image2= models.ImageField(blank = True)
    image3 = models.ImageField(blank = True)
    image4= models.ImageField(blank = True)


    def __str__(self):
        return  self.title

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return  self.comment[0:15] +"..."+ "by " + self.user.username