from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from apps.comments.models import Comments
from apps.cards.models import Cards
from apps.users.models import UserProfile
# Create your views here.


@login_required(login_url='/users/login/')
def comment(request, card_id):
    """Business Logic for Comment."""
    context = {}
    if request.method == 'POST':
        try:
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)
            comment = request.POST.get('card_comment')
            card = Cards.objects.get(id=card_id)

            comment_info = Comments(
                user_profile=created_by,
                cards=card,
                comments=comment)

            comment_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/%s/" % card_id, context)
