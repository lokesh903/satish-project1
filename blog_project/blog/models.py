from django.db import models
import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.ImageField(upload_to='images/')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published_date=models.DateField()


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=1000)
    created_date=models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.post