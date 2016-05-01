"""Models Defenition."""
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
GENDER_CHOICES = (('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female'))


class UserProfile(models.Model):
    """Saving registered users."""

    user = models.OneToOneField(
        User,
        verbose_name="related user")

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Name')

    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name='Email')

    joining_date = models.DateTimeField(
        'Date Joined',
        default=datetime.datetime.now)

    def __unicode__(self):
        """Unicode class."""
        return self.name

    class Meta:
        """Information About the class."""

        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"


class UserProfileInfo(models.Model):
    """Class to store User Profile."""

    user = models.OneToOneField(UserProfile)

    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)

    full_name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        null=True)

    profile_picture = models.ImageField(upload_to='uploaded_files')

    def __unicode__(self):
        """Unicode method to display Username in Admin."""
        return self.user.username

    class Meta:
        """Information About the class."""

        verbose_name = "UserProfileInfo"
        verbose_name_plural = "UserProfileInfo"
