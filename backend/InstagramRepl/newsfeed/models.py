from django.db import models

from user.models import Profile

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField()
    description = models.CharField(max_length=250)


class Comment(models.Model):
    text = models.CharField(max_length=250)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Like(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
