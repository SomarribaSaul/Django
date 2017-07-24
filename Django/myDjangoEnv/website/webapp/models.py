from django.db import models


# Create your models here.
class User(models.Model):
    full_name= models.CharField(max_length= 120)
    email= models.EmailField(max_length=264, unique= True)

    def __str__(self):
        return self.full_name
