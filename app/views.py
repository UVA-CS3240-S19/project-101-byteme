from django.shortcuts import render, redirect


def home(request):
    context = {
        
    }
    if not request.user.is_authenticated:
        return redirect('login') 
    else:
        return render(request, 'app/main_page.html', context)


def sign_up(request):
    context = {}
    return render(request, 'app/sign_up.html', context)


def profile(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login') 
    else:
        return render(request, 'app/profile.html', context)

def login(request):
    context = {}
    return render(request, 'app/login_page.html', context)

