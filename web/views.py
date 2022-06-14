from django.shortcuts import render

from web.models import Card


def index(request):
    cards = Card.objects.all()

    return render(request, 'index.html', {'cards': cards})


def detail(request, pk):
    card = Card.objects.get(id=pk)

    context = {'card': card}
    return render(request, 'detail.html', context=context)

def about(request):
    return render(request, 'about.html')
