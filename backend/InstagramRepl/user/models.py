from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Following = models.ManyToManyField(
        "self", related_name="following", blank=True)
    Followers = models.ManyToManyField(
        "self", related_name="follower", blank=True)
    profile_photo = models.ImageField(
        default='uploads/profile/defaultimage.png', upload_to='uploads/profile/', blank=True)
    DOB = models.DateField(default=datetime.date.today, blank=True, null=True)

    def __str__(self):
        return self.user.username
