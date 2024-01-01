from django.urls import path, reverse_lazy
from . import views

app_name = 'twitter'
urlpatterns = [   
    path('register/', views.RegisterView.as_view(), name = 'register'),
    
    path('', views.ListView.as_view(), name='list'),    
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    path('<int:pk>/update', views.UpdateView.as_view(success_url=reverse_lazy('twitter:list')), name='update'),
    path('<int:pk>/delete', views.DeleteView.as_view(success_url=reverse_lazy('twitter:list')), name='delete'),
    
    path('create/', views.CreateView.as_view(success_url=reverse_lazy('twitter:list')), name='create'),
    
]