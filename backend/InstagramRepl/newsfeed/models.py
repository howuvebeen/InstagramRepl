from django.db import models

from user.models import Profile

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/post/', null=True)
    description = models.CharField(max_length=250)
    owner = models.ForeignKey('auth.User', related_name= 'posts', on_delete= models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=250)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name= 'comments', on_delete= models.CASCADE)

    def __str__(self):
        return self.text


class Like(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey('auth.User', related_name= 'likes', on_delete= models.CASCADE)
