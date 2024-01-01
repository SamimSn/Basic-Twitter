from math import e
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect

from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerListView, OwnerDetailView
from .models import Twitt

from django.contrib.auth.models import User
from .forms import Register

# Create your views here.

class CreateView(OwnerCreateView):
    model = Twitt
    fields = ['text']
    
class UpdateView(OwnerUpdateView):
    model = Twitt
    fields = ['text']    
    
class DeleteView(OwnerDeleteView):
    model = Twitt
    
class ListView(OwnerListView):
    model = Twitt
    
class DetailView(OwnerDetailView):
    model = Twitt


class RegisterView(View):    
    
    def get(self, req):
        return render(req, 'registration/register.html', {
            'form': Register()          
        })
    
    def post(self, req):                
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect(reverse_lazy('login'))        
        else:
            return render(req, 'registration/register.html', {
                'msg': 'username or email already taken.',
                'form': Register()
            })         
        
        