"""Models Defenition."""
from django.db import models
from apps.users.models import UserProfile
from django.utils import timezone
# Create your models here.


class Cards(models.Model):
    """docstring for cards."""

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='card',
        default="")

    card_hero_image = models.ImageField(
        upload_to='Cards',
        blank=True,
        null=True,
        verbose_name='Card display image',
        help_text='Add')

    card_title = models.CharField(
        max_length=255,
        blank=False,
        null=False,)
    card_created_on = models.DateTimeField(
        'date published',
        default=timezone.now)

    card_description = models.TextField(
        blank=False,
        null=False,
        verbose_name='card_description')

    def __unicode__(self):
        """Unicode Method to Display Relevent data in Admin."""
        return self.card_title

    class Meta:
        """Information About the class."""

        verbose_name = "Cards"
        verbose_name_plural = "Cards"
