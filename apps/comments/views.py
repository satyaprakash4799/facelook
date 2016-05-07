from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
# from apps.comments.models import Comments
from apps.cards.models import Cards
from apps.users.models import UserProfile
from apps.comments.forms import CommentsForm
# Create your views here.


@login_required(login_url='/users/login/')
def comment(request, card_id):
    """Business Logic for Comment."""
    import ipdb; ipdb.set_trace()
    context = {}
    form = CommentsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)
            comment.user_profile = created_by
            card = Cards.objects.get(id=card_id)
            comment.cards = card
            comment.save()

            context = {'success': True, 'message': 'Successfully Saved'}
        else:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/%s/" % card_id, context)
