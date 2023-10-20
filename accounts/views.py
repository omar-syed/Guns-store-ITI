from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.contrib.auth.models import  User
from . forms import  CustomizedUserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None): #Returns the single object that this view will display.
        return self.request.user         #return the currently logged-in user   

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile_edit.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('register')

    def get_object(self, queryset=None):
        return self.request.user


class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/registeration.html'
    form_class = CustomizedUserCreationForm
    # login_url = reverse('login')
    success_url = reverse_lazy("login")