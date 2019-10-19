from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=15,blank=True)
    content = models.TextField(default='')
    date_posted = models.DateTimeField(default =  timezone.now)
    author = models.ForeignKey(User,   on_delete=models.CASCADE)