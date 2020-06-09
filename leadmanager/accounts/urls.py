from django.urls import path, include
from knox.views import LogoutView

from .apis import RegisterAPI, LoginAPI, UserAPI


urlpatterns = [
    path('', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', LogoutView.as_view(), name='knox_logout'),
]
