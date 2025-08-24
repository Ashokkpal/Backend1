from django.db import models

# Create your models here.

class student(models.Model):
    # id=models.AutoField(_(""))
    name=models.CharField()
    age=models.IntegerField()
    email=models.EmailField()
    addres=models.TextField(null=True,blank=True)
    # image=models.ImageField()
    # file=models.FileField()
    # college=models.TextField()


class car(models.Model):
    car_name=models.CharField(max_length=50)
    speed=models.IntegerField(default=50)

def __str__(self)->str:
    return self.car_name
