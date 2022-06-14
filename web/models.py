from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment - {self.date}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'