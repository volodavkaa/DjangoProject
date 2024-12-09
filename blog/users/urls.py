from django.urls import path
from .views import register, CustomLoginView, profile
from django.contrib.auth.views import LogoutView
from users.forms import UserLoginForm
urlpatterns = [
    path('register/', register, name='register'),  
    path('login/', CustomLoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('profile/', profile, name='profile'),  
]
