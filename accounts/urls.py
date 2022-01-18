from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('login/',  auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',  auth_views.LogoutView.as_view(next_page='cars:index'), name='logout'),
    path('api/', include('accounts.apiurls')),
]
