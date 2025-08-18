from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done')  
]