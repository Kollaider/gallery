from django.urls import path

from web.views import index, detail, about, do_comment, WebLoginView, WebLogoutView

app_name = "web"
urlpatterns = [
    path('login/', WebLoginView.as_view(), name='login'),
    path('logout/', WebLogoutView.as_view(), name='logout'),
    path('comment/<int:card_pk>', do_comment, name='comment'),
    path('', index, name="home"),
    path('detail/<int:pk>', detail, name="detail"),
    path('about/', about, name='about'),
]
