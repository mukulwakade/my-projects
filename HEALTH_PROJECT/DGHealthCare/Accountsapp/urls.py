from django.urls import path
from .views import signupView,loginView,logoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/',signupView,name='signup'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name='password_reset_complete'),
    
]