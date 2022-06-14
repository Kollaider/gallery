from django.urls import path

from web.views import index, detail, about

app_name = "web"
urlpatterns = [
    path('', index, name="home"),
    path('detail/<int:pk>', detail, name="detail"),
    path('about/', about, name='about')
]