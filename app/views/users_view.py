import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseServerError
from django.views import View
from app.models import Users, Teams
import bcrypt
from app.views.auth_view import LoginRequired

# READ
class UsersList(LoginRequired, View):
    def get(self, request):
        try :
            users = Users.objects.select_related('team').values('id', 'username', 'created', 'updated', 'team__name')
            return render(request, template_name='users/users_list.html', 
                        context={'users' : users})
        except Exception:
            return HttpResponseServerError("Impossible de charger la liste d'utilisateurs")

# CREATE 
class UsersCreate(LoginRequired, View):
    def get(self, request):
        error = request.GET.get('error', False)
        return render(request, template_name='users/users_create.html', 
                      context={'error': error})
    
    def post(self, request):
        try :
            username = request.POST["username"]
            password = request.POST["password"]

            if len(username) > 20 or len(password) > 20 or len(username) < 8 or len(password) < 8:
                return redirect(reverse('users_create') + f'?error=true')

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            user = Users.objects.create(username=username, password=hashed_password)
            user.save()

            return redirect('users_list')
        except Exception:
            return HttpResponseServerError("Echec de la création de l'utilisateur");

# DELETE
class UsersDelete(LoginRequired, View):
    def get(self, request, id):
        try :
            user = Users.objects.get(id=id)
            user.delete()

            return redirect('users_list')  
        except Exception:
            return HttpResponseServerError("Echec de la suppression de l'utilisateur")
    
# UPDATE
class UsersUpdate(LoginRequired, View):
    def get(self, request, id):
        error = request.GET.get('error', False)
        try :
            user = Users.objects.get(id=id)

            return render(request, template_name='users/users_update.html',
                        context={'user': user, 'error': error})
        except Exception:
            return HttpResponseServerError("Echec du chargement de l'utilisateur")
    
    def post(self, request, id):
        try :
            username = request.POST["username"]

            if len(username) > 20 or len(username) < 8:
                return redirect(reverse('users_update', args=[id]) + f'?error=true')

            user = Users.objects.get(id=id)
            user.username = username
            user.save()

            return redirect('users_list')
        except Exception:
            return HttpResponseServerError("Echec de la modification de l'utilisateur");

# ADD TEAM TO USERS
class UsersShuffle(LoginRequired, View):
    def get(self, request):
        try:
            users = list(Users.objects.all())
            teams = Teams.objects.all()

            teams_ids = list(teams.values_list('id', flat=True))
            random.shuffle(teams_ids)
            random.shuffle(users)

            index = 0
            for user in users:
                user.team = Teams.objects.get(id=teams_ids[index])
                user.save()

                if (index + 1) < len(teams_ids):
                    index += 1
                else:
                    index = 0
                
            return redirect('users_list')
        except Exception as e:
            print(e)
            return HttpResponseServerError("Impossible de mélanger les utilisateurs dans des équipes")

# RESET TEAMS TO USERS
class UsersReset(LoginRequired, View):
    def get(self, request):
        try:
            users = list(Users.objects.all())

            for user in users:
                user.team = None
                user.save()

            return redirect('users_list')
        except Exception:
            return HttpResponseServerError("Impossible de réinitialiser les équipes des utilisateurs")