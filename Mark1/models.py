from django.db import models

# Create your models here.
class login(models.Model):
    userid = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)


    def __str__(self):
        return self.userid



class sent(models.Model):
    select = models.CharField(max_length=20)
    message = models.CharField(max_length=2000)
    times = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    checkbox = models.CharField(max_length=20)
    message1 = models.CharField(max_length=2000)
    slt2 = models.CharField(max_length=20)
    message2 = models.CharField(max_length=2000)
    message3 = models.CharField(max_length=2000)


    def __str__(self):
        return self.select