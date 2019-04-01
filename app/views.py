from django.contrib.auth import logout
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
    # HttpResponseRedirect(reverse('update_profile', kwargs={"pk": request.user.id}))


def search(request):
    print("body", request.body)
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.POST['search_field'] == "":
            return render(request, 'app/search_results.html', {'search_value': "", 'results': Profile.objects.all()})
        search_value = request.POST['search_field']
        search_value = str(search_value).lower().strip()
        results = set()
        for profile in Profile.objects.all():

            profile_name = profile.name.lower().split(" ")
            # or search_value == profile_name[1]:
            if search_value == profile.name.lower() or search_value == profile_name[0]:
                results.add(profile)

            for tags in profile.tags.all():
                if search_value == str(tags).lower():
                    results.add(profile)
        return render(request, 'app/search_results.html', {'search_value': search_value, 'results': results})

# form to create profile


def create_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        computing_id = request.user.email
        ind = computing_id.index('@')
        computing_id = computing_id[0:ind]
        ProfileModel = modelform_factory(Profile, fields=(
            'name', 'year', 'major', 'bio', 'skills', 'courses', 'organizations', 'interests'))
        if request.method == "POST" or Profile.objects.filter(user_id=computing_id):
            form = ProfileModel(request.POST)
            if (form.is_valid()):
                profile = form.save(commit=False)
                profile.user_id = computing_id
                profile.id = request.user.id
                # profile.save()
                # 'computing_id':computing_id}))

                tags_to_add = set()

                skills_list = profile.skills.split(",")
                for i in skills_list:
                    tags_to_add.add(i.strip())

                interests_list = profile.interests.split(",")
                for i in interests_list:
                    tags_to_add.add(i.strip())

                for i in tags_to_add:
                    profile.tags.add(i)

                profile.save()
                return HttpResponseRedirect(reverse('app:published_profile', kwargs={'pk': profile.id}))
            else:
                return HttpResponseRedirect(reverse('app:published_profile', kwargs={'pk': request.user.id}))

        else:
            return render(request, 'app/profile.html', {'form': ProfileModel()})

        # if request.method == "POST":
        #     profile = ProfileForm(request.POST)
        #     if profile.is_valid():
        #         profile.save()
        #         profile.id = request.user.id
        #         profile.save()
        #         return HttpResponseRedirect(reverse('app:published_profile', kwargs={'pk': profile.id}))
        #     else:
        #         return render(request, 'app/profile.html', {'form': ProfileForm()})
        # else:
        #     return render(request, 'app/profile.html', {'form': ProfileForm()})
'''
def update_profile(request, pk):

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        computing_id = request.user.email
        ind = computing_id.index('@')
        computing_id = computing_id[0:ind]
        UpdateProfileForm = modelform_factory(Profile, fields=(
            'name', 'year', 'major', 'bio', 'skills', 'courses', 'organizations', 'interests'))
        # UpdateProfileForm = modelform_factory(Profile, fields=('name', 'year', 'major', 'bio', 'skills', 'courses','organizations', 'interests'))
        if request.method == "POST" or Profile.objects.filter(user_id = computing_id):
            profile = UpdateProfileForm(request.POST, instance=request.user)
            if (profile.is_valid()):
                profile.save()
                return HttpResponseRedirect(reverse('app:update_profile', kwargs={'pk': pk}))
            else:
                return render(request, 'app/published_profile.html', {'form': ProfileModel()})
        else:
            profile = UpdateProfileForm()
            return render(request, 'app/published_profile.html', {'form': profile})

        #     if request.method == "POST":
        #         profile = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        #
        #         if profile.is_valid():
        #             profile.save()
        #
        #         return HttpResponseRedirect(reverse('app:update_profile', kwargs={'pk': pk}))
        #     else:
        #         profile = UpdateProfileForm(instance=request.user)
        #         return render(request, 'app/published_profile.html', {'form': profile})
        '''


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


def logout_view(request):
    logout(request)
    return render(request, 'app/login_page.html')
