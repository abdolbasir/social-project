from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout')     
]