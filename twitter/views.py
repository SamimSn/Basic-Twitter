from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerListView, OwnerDetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Twitt

# Create your views here.

class TwittCreateView(SuccessMessageMixin, OwnerCreateView):
    model = Twitt
    fields = ['text']
    success_message = "Twitt created"
    
class TwittUpdateView(SuccessMessageMixin, OwnerUpdateView):
    model = Twitt
    fields = ['text']    
    success_message = "Twitt updated"
    
class TwittDeleteView(SuccessMessageMixin, OwnerDeleteView):
    model = Twitt    
    success_message = "Twitt deleted"
    
class TwittListView(OwnerListView):
    model = Twitt
    
class TwittDetailView(OwnerDetailView):
    model = Twitt   

class RegisterView(SuccessMessageMixin ,CreateView):    
    model = User
    template_name = 'registration/register.html'    
    form_class =  UserCreationForm     
    success_message = "User added"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)        
        for field in form.fields.keys():
            form[field].help_text = None
        return form                        


class UserTwittsListView(OwnerListView):
    model = Twitt        
        
    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Twitt.objects.filter(owner=user)
    
    def get_context_data(self, **kwargs):
        context = super(UserTwittsListView, self).get_context_data(**kwargs)        
        context['user_twitts_list'] = True               
        return context  