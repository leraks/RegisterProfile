from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    GENDORS = (

        ('M', 'MEN'),
        ('F', 'WOME'),

    )

    email_tag = models.CharField(max_length=30,blank=True,null=True,default='')
    gender = models.CharField(choices=GENDORS,max_length=1,default='MEN',blank=True,null=True)

    def __str__(self):
        return self.username