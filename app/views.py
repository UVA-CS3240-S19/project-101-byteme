from django.shortcuts import render


def home(request):
    context = {
        
    }
    return render(request, 'app/main_page.html', context)


def sign_up(request):
    context = {}
    return render(request, 'app/sign_up.html', context)


def profile(request):
    context = {}
    return render(request, 'app/profile.html', context)

