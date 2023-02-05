from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def logs_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('index')
        else:
            messages.error(
                request, 'There was an error login you in please check details')
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})

# Create your views here.


def logout_user(request):
    logout(request)
    messages.success(request, ('you have been logged out'))
    return redirect('login')
