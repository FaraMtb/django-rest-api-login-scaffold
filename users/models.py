from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    client_Id = models.PositiveIntegerField(null=True,blank=True)
    middle_name = models.CharField(null=True,blank=True, max_length=250)
    is_employee = models.BooleanField(default=False, blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    def my_fullname(self):
            if self.middle_name:
              return self.first_name+" "+self.middle_name+" "+self.last_name

            return self.first_name+" "+self.last_name

    fullname = property(my_fullname)
