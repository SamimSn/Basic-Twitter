from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect

from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerListView, OwnerDetailView
from .models import Twitt

from django.contrib.auth.models import User
from .forms import Register

from django.contrib import messages

# Create your views here.

class TwittCreateView(OwnerCreateView):
    model = Twitt
    fields = ['text']
    
class TwittUpdateView(OwnerUpdateView):
    model = Twitt
    fields = ['text']    
    
class TwittDeleteView(OwnerDeleteView):
    model = Twitt    
    
class TwittListView(OwnerListView):
    model = Twitt
    
class TwittDetailView(OwnerDetailView):
    model = Twitt    


class RegisterView(View):    
    
    def get(self, req):
        return render(req, 'registration/register.html', {
            'form': Register()          
        })
    
    def post(self, req):                
        form = Register(req.POST)
                
        if form.is_valid():            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)         
            user.save()
            messages.success(req, 'user has been added successfully')
            return redirect(reverse_lazy('login'))        
        else:            
            messages.warning(req, f'{form.errors}')
            return render(req, 'registration/register.html', {                
                'form': Register()
            })      


class UserTwittsListView(OwnerListView):
    model = Twitt        
        
    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Twitt.objects.filter(owner=user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add extra context data
        context['user_twitts_list'] = True 
        context['username'] = self.kwargs.get('username')       
        return context  