from django.shortcuts import render

from web.models import Card, Comment


def index(request):
    cards = Card.objects.all()

    return render(request, 'index.html', {'cards': cards})


def detail(request, pk):
    card = Card.objects.get(id=pk)
    comments = Comment.objects.filter(card_id=pk)
    print(comments.query)
    context = {'card': card, 'comments': comments}
    return render(request, 'detail.html', context=context)

def about(request):
    return render(request, 'about.html')
