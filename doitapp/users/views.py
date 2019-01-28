from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from users.models import Profile

from django.db.utils import IntegrityError

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            print ("Usuario logueado")
            return redirect('/tasks/')
        else:
            print ("Error de inicio de sesion")
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    else:
        return render(request, 'users/login.html')
        
@login_required
def logoutView(request):
    """Logout a user"""
    logout(request)
    return redirect('login')

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
