from django.db import models

# Create your models here.
class Customer(models.Model):
    fullname= models.CharField(max_length=30)
    age= models.SmallIntegerField()
    telephone= models.IntegerField()
    email=models.EmailField()
    order=models.DateTimeField()

    def __str__(self):
        return self.fullname
    