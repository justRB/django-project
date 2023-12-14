import bcrypt
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from app.models import Users
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# USER LOGIN
class UserLogin(View):
    def get(self, request):
        error = request.GET.get('error', False)
        return render(request, template_name='auth/login.html',
                      context={'error': error})
    
    def post(self, request):
        try:
            username = request.POST["username"]
            password = request.POST["password"]

            user = Users.objects.get(username=username)

            verified_password = bcrypt.checkpw(password.encode('utf-8'), user.password)

            if verified_password:
                login(request, user)
                return redirect('app_home')
            else:
                return redirect(reverse('auth_login') + f'?error=true')
        except Users.DoesNotExist:
            return redirect(reverse('auth_login') + f'?error=true')
        
# USER LOGOUT
class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('auth_login')

# LOGIN REQUIRED REDIRECTION
class LoginRequired:
    @method_decorator(login_required(login_url='auth_login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)