from django.urls import path, include
from knox.views import LogoutView

from .apis import RegisterAPI, LoginAPI, UserAPI


urlpatterns = [
    path('', include('knox.urls')),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('user', UserAPI.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
]
