from django.views.generic import ListView, DetailView
from registration.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ProfileListView(ListView):
    model = Profile
    template_name = 'Profiles/profile_list.html'
    # context_object_name = 'profiles'

    #def get_queryset(self):
        #return Profile.objects.select_related('user').all()

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Profiles/profile_detail.html'
    #context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])