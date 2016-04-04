from django.core.context_processors import csrf
from django.shortcuts import render

from apps.cards.models import Cards
# Create your views here.


def all_cards(request):
    """Display all cards."""
    context = {}
    cards = Cards.objects.all()
    context = {'cards': cards}
    template = 'all_cards.html'
    context.update(csrf(request))
    return render(request, template, context)


def view_card(request, card_id):
    """Display specific card."""
    context = {}
    card = Cards.objects.get(id=card_id)
    context = {'card': card}
    template = 'view_card.html'
    context.update(csrf(request))
    return render(request, template, context)
