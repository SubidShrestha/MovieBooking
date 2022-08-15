from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        
        # if not email:
        #     raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class user(AbstractUser):
    username = None
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    email = models.EmailField(max_length=254,unique=True)
    GENDER=[('Male','Male'),('Female','Female'),('Other','Other')]
    gender= models.CharField(max_length=6,choices=GENDER,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["gender","first_name","last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email