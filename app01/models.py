from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)  # string
    email = models.EmailField()  # string 帮admin做输入验证，modelform
    memo = models.TextField()  # text
    img = models.ImageField()
    user_type = models.ForeignKey(UserType,null=True,blank=True,on_delete=models.CASCADE)
