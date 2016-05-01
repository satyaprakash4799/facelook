"""URL configuration for Cards."""
from django.conf.urls import url
from apps.cards.views import view_card, all_cards, create_card

urlpatterns = [
    url(r'^$', all_cards),
    url(r'^(?P<card_id>\d+)/$', view_card),
    url(r'^create_card/$', create_card),
]
