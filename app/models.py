from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.address

# Models for EmailOTP:
class EmailOTP(models.Model):

    otp = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() - self.created_at < datetime.timedelta(minutes=5)  # 5 minutes validity