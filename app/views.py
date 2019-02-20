from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.forms import modelform_factory
from django.views import generic
from django.urls import reverse

from .models import Profile, ProfileModel

# published profile view
class ProfileView(generic.ListView):
    template_name = 'app/published_profile.html'
    context_object_name = 'profile_attributes'

    def get_queryset(self):
        return Profile.objects.all()

# form to create profile
def create_profile(request):
    ProfileModel = modelform_factory(Profile, fields=('name', 'year', 'major', 'bio', 'skills', 'courses','organizations', 'interests'))
    if request.method == "POST":
        form = ProfileModel(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('app:published_profile'))
        else:
            return render(request, 'app/profile.html', {'form': ProfileModel()})

    else:
        return render(request, 'app/profile.html', {'form': ProfileModel()})

def news_feed(request):

    return render(request, 'app/news_feed.html')

# def home(request):
#     context = {
#
#     }
#     return render(request, 'app/main_page.html', context)
#
#
# def sign_up(request):
#     context = {}
#     return render(request, 'app/sign_up.html', context)
#
#
# def profile(request):
#     context = {}
#     return render(request, 'app/profile.html', context)
#
#
# def login(request):
#     context = {}
#     return render(request, 'app/login_page.html', context)