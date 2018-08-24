from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name='用户名')  # string
    email = models.EmailField(db_index=True)  # string 帮admin做输入验证，modelform
    memo = models.TextField()  # text
    img = models.ImageField()
    user_type = models.ForeignKey(UserType, null=True, blank=True, on_delete=models.CASCADE)
    #user_type = models.OneToOneField(UserType,null=True,blank=True,on_delete=models.CASCADE)   #OneToOne
    #ctime = models.DateTimeField(auto_now_add=True)
    #updata_time = models.DateTimeField(auto_now=True)

    gender_choices = (
        (0,'男'),
        (1,'女')
    )
    Gender = models.IntegerField(choices=gender_choices,default=1)


'''
# ManyToMany
class B2G(models.Model):
    boy = models.ForeignKey('Boy')
    girl = models.ForeignKey('Girl')


class Boy(models.Model):
    name = models.CharField(max_length=32)

class Girl(models.Model):
    name = models.CharField(max_length=32)

    #f = models.ManyToManyField(Boy)
'''
