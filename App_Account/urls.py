from django.urls import path
from App_Account import views
app_name='App_Account'

urlpatterns = [
    path('signup', views.SignupView, name='signup'),
    # path('login', views.loginview, name='login'),
    # path('login-out', views.Logout, name='logout'),
    # path('profile-update', views.profileupdate, name='profileupdate'),
]
