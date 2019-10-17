from django.db import models

# Create your models here.
class AddUser(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    username = models.CharField(max_length=40,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="static/images")

    def __str__(self):
        return "{}".format(self.email)




