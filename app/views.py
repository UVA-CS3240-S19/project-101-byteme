from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.forms import modelform_factory
from django.views import generic
from django.urls import reverse
from .models import Profile, ProfileModel, Post, UpdateProfileForm

def home(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login') 
    else:
        return redirect('profile')

def news_feed(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'app/news_feed.html', context)

# published profile view
class ProfileView(generic.DetailView):
    template_name = 'app/published_profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.all()

class UpdateView(generic.DetailView):
    template_name = 'app/update_profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.all()

def update_profile(request, pk):
    return render(request, 'app/update_profile.html')
    #HttpResponseRedirect(reverse('update_profile', kwargs={"pk": request.user.id}))

# form to create profile
def create_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        computing_id = request.user.email
        ind = computing_id.index('@')
        computing_id = computing_id[0:ind]
        ProfileModel = modelform_factory(Profile, fields=('name', 'year', 'major', 'bio', 'skills', 'courses','organizations', 'interests'))
        if request.method == "POST" or Profile.objects.filter(user_id = computing_id):
            form = ProfileModel(request.POST)
            if (form.is_valid()):
                profile = form.save(commit=False)
                profile.user_id = computing_id
                profile.id=request.user.id
                profile.save()
                return HttpResponseRedirect(reverse('app:published_profile', kwargs={'pk': profile.id}))#'computing_id':computing_id}))
            else:
                return HttpResponseRedirect(reverse('app:published_profile', kwargs={'pk': request.user.id}))

        else:
            return render(request, 'app/profile.html', {'form': ProfileModel()})

def login(request):
    context = {}
    return render(request, 'app/login_page.html', context)

def messaging(request):
    return render(request, 'app/messaging.html')

def notifications(request):
    return render(request, 'app/notifications.html')

def friends(request):
    return render(request, 'app/friends.html')

def settings(request):
    return render(request, 'app/settings.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'app/login_page.html')
