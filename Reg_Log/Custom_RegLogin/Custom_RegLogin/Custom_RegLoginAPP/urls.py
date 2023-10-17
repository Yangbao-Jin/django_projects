from django.urls import path
from .views import CustomLoginView, CustomRegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('register/', CustomRegisterView.as_view(), name='custom_register'),
]
