from django.urls import path, reverse_lazy
from . import views

app_name = 'twitter'
urlpatterns = [   
    path('register/', views.RegisterView.as_view(), name = 'register'),
    
    path('', views.TwittListView.as_view(), name='list'),    
    path('<int:pk>/', views.TwittDetailView.as_view(), name='detail'),    
    
    path('<int:pk>/update/', views.TwittUpdateView.as_view(success_url=reverse_lazy('twitter:list')), name='update'),
    path('<int:pk>/delete/', views.TwittDeleteView.as_view(success_url=reverse_lazy('twitter:list')), name='delete'),
    
    path('create/', views.TwittCreateView.as_view(success_url=reverse_lazy('twitter:list')), name='create'),
    
    path('<str:username>/', views.UserTwittsListView.as_view(), name='user_twitts_list'),
    
]