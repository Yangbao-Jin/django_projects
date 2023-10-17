

# Create your views here.
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'custom_login.html'
    
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView

class CustomRegisterView(FormView):
    template_name = 'custom_register.html'
    form_class = UserCreationForm
    success_url = '/login/'  # 重定向到登录页面

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
