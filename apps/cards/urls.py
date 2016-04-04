"""URL configuration for Cards."""
from django.conf.urls import url
from apps.cards.views import view_card, all_cards

urlpatterns = [
    url(r'^$', all_cards),
    url(r'^(?P<card_id>\d+)/$', view_card),
]
