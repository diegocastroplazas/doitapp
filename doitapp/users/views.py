from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin


"""Models"""
from users.models import Profile

class LoginView(auth_views.LoginView):
    template_name = 'users/form.html'

class LogoutView( LoginRequiredMixin, auth_views.LogoutView):
    next_page = '/users/login'

# Create your views here.


def signupView(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwdConfirmation']
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username = username, password = passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})
        user.first_name = request.POST['firstName']
        user.last_name = request.POST['lastName']
        user.save()
        profile = Profile(user=user)
        profile.save()
        
        return redirect('/users/login.html')

    else:
        return render(request, 'users/signup.html')

def updateProfile(request):
    return render(request, 'users/updateProfile.html')



