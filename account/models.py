from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Create your models here.


class CustomUserManager(UserManager):
    def create_user(self, email, first_name, last_name, password=None,  **extra_fields):

        if not email:
            raise ValueError('You did not provide a valid email address')
        
        if not first_name:
            raise ValueError('Provide first name')
        
        if not last_name:
            raise ValueError('Provide last name') 
        
        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, 
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email=email, first_name=first_name, 
                                last_name=last_name,
                                password=password,
                                **extra_fields)




# class CustomUser(AbstractBaseUser, PermissionsMixin):
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    last_name= models.CharField(max_length=225, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']