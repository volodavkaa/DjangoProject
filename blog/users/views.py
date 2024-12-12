from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, f'Ласкаво просимо, {user.username}!')
            return redirect('homepage')  
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'  

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super().dispatch(request, *args, **kwargs)

@login_required
def profile(request):
    return render(request, 'users/profile.html')
