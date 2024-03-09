from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
