from django.core.context_processors import csrf
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from apps.cards.models import Cards
from apps.users.models import UserProfile
from apps.comments.models import Comments
from apps.comments.forms import CommentsForm
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
    import ipdb; ipdb.set_trace()
    context = {}
    card = Cards.objects.get(id=card_id)
    comments = Comments.objects.filter(cards=card)
    form = CommentsForm()
    context = {'card': card, 'comments': comments, 'form': form}
    template = 'view_card.html'
    context.update(csrf(request))
    return render(request, template, context)


@login_required(login_url='/users/login/')
def create_card(request):
    """Creating new cards."""
    context = {}
    if request.method == 'POST':
        try:

            card_title = request.POST.get('card_title')
            card_description = request.POST.get('card_description')
            card_picture = request.FILES.get('card_picture')
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)

            card_info = Cards(
                card_title=card_title,
                user_profile=created_by,
                card_description=card_description,
                card_hero_image=card_picture)

            card_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    template = "create_card.html"
    return render(request, template, context)
