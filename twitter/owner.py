from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """ Some Text """
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """ Some Text """    
    
    def get_queryset(self):        
        return super(OwnerUpdateView, self).get_queryset().filter(owner=self.request.user)
    
class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """ Some Text """
    
    def get_queryset(self):        
        return super(OwnerDeleteView, self).get_queryset().filter(owner=self.request.user)
    
class OwnerListView(LoginRequiredMixin, ListView):
    """ Some Text """
    
class OwnerDetailView(LoginRequiredMixin, DetailView):
    """ Some Text """
    