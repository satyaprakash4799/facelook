"""Model class for comments app."""
from django.db import models
from apps.users.models import UserProfile
from apps.cards.models import Cards
# Create your models here.


class Comments(models.Model):
    """Comments for cards."""

    user_profile = models.ForeignKey(
        UserProfile,
        default="",
        null=False,
        blank=False)

    cards = models.ForeignKey(
        Cards,
        default="",
        null=False,
        blank=False)

    comments = models.TextField(
        null=False,
        blank=False,
        default="",
        verbose_name='Comments',
        help_text='You can give your thoughts for the card.')

    def __unicode__(self):
        """Unicode for Comments."""
        return str(self.cards.card_title)
