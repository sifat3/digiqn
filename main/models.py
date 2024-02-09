from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Request(models.Model):
    sender_name = models.CharField(max_length=200, blank=False, null=False)
    receiver_name = models.CharField(max_length=200, blank=False, null=False)
    sender_email = models.EmailField(blank=False, null=False)
    receiver_email = models.EmailField(blank=False, null=False)
    ammount = models.IntegerField(blank=False, null=False)
    service_description = models.TextField()
    payment_done = models.BooleanField(default=False)
    service_done = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=500, blank=True, null=True)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)




