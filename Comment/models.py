from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Message(models.Model):

    user = models.ForeignKey(User,on_delete= models.CASCADE)
    content = models.TextField("內容")
    publication_date = models.DateTimeField("留言日期", auto_now_add=True)
