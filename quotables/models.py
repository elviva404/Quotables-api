from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user
    
    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name =  models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    quotes = models.ManyToManyField("Quote", related_name="+", blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve FullName of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    
    def __str__(self):
        """Return String representation of user"""
        return self.email

    def __str__(self):
        return self.name

class Category(models.Model): 
    name = models.CharField(max_length=255)
    quotes = models.ManyToManyField("Quote", related_name="+", blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model): 
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="+", 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    quotes = models.ManyToManyField("Quote", related_name="+", blank=True)
    profile_image_url = models.FileField(
        upload_to="media/artist/", blank=True, null=True
    )

    def __str__(self):
        return self.name

class Mood(models.Model): 
    name = models.CharField(max_length=255)
    quotes = models.ManyToManyField("Quote", related_name="+", blank=True)
    image_url = models.FileField(
        upload_to="media/mood/", blank=False, null=True
    )

    def __str__(self):
        return self.name

class Quote(models.Model): 
    quote = models.TextField()
    song_title = models.CharField(max_length=255)

    artist = models.ForeignKey(
        Artist, related_name="+", 
        on_delete=models.CASCADE
    )
    contributor = models.ForeignKey(
        User, related_name="+", 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, related_name="+", 
        on_delete=models.CASCADE
    )

    mood = models.ManyToManyField("Mood", related_name="+", blank=False)

    apple_music_url = models.URLField(max_length=255, blank=True, null=True)
    spotify_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.quote