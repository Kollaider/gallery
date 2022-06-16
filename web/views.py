from django.shortcuts import render, redirect
from django.urls import reverse

from web.models import Card, Comment


def index(request):
    cards = Card.objects.all()

    return render(request, 'index.html', {'cards': cards})


def detail(request, pk):
    card = Card.objects.get(id=pk)
    comments = Comment.objects.filter(card_id=pk).order_by('-date')
    print(comments.query)
    context = {'card': card, 'comments': comments}
    return render(request, 'detail.html', context=context)

def about(request):
    return render(request, 'about.html')


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm

def do_comment(request, card_pk):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        print(str(form.errors))
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            new_comment = Comment(user_id=request.user.id, card_id=card_pk)
            new_comment.text = form.cleaned_data['comment']
            new_comment.save()
            return HttpResponseRedirect(reverse('web:detail', args=[card_pk]))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render(request, 'detail.html', {'form': form})