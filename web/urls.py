from django.urls import path

from web.views import index, detail, about, do_comment

app_name = "web"
urlpatterns = [
    path('comment/<int:card_pk>', do_comment, name='comment'),
    path('', index, name="home"),
    path('detail/<int:pk>', detail, name="detail"),
    path('about/', about, name='about'),
]
