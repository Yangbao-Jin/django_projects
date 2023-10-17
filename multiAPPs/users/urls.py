from django.urls import path
from .views import register,UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
   # path('register/', register, name='register'),
    path('', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]

