from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Following = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    Followers = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    profile_photo = models.ImageField(null= True)
    DOB = models.DateField()

    def __str__(self):
        return user.username