from django.urls import path
from . import views

urlpatterns = [
    path('simplify/', views.simplify_expression, name='simplify_expression'),
]
