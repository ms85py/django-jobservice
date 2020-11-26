from django.shortcuts import render, redirect
from django.views import View


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/menu.html')


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = '/home'
    template_name = 'menu/login.html'


class UserView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'menu/user_view.html')
        else:
            return redirect('/login')