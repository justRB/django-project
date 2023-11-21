from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseServerError
from django.views import View
from app.models import Users

# READ 
class UsersList(View):
    def get(self, request):
        try :
            users = Users.objects.values('id', 'username', 'created', 'updated')
            return render(request, template_name='users_list.html', 
                        context={'users' : users})
        except Exception:
            return HttpResponseServerError("Erreur 500 : Impossible de charger la liste d'utilisateurs")

# CREATE 
class UsersCreate(View):
    def get(self, request):
        error = request.GET.get('error', False)
        return render(request, template_name='users_create.html', 
                      context={'error': error})
    
    def post(self, request):
        try :
            username = request.POST["username"]
            password = request.POST["password"]

            if len(username) > 20 or len(password) > 20 or len(username) < 8 or len(password) < 8:
                return redirect(reverse('users_create') + f'?error=true')

            user = Users.objects.create(username=username, password=password)
            user.save()
            return redirect('users_list')
        except Exception:
            return HttpResponseServerError("Erreur 500 : Echec de la création de l'utilisateur");

# DELETE
class UsersDelete(View):
    def get(self, request, id):
        try :
            user = Users.objects.get(id=id)
            user.delete()
            return redirect('users_list')  
        except Exception:
            return HttpResponseServerError("Echec de la suppression de l'utilisateur")
    
# UPDATE
class UsersUpdate(View):
    def get(self, request, id):
        error = request.GET.get('error', False)
        try :
            user = Users.objects.get(id=id)
            return render(request, template_name='users_update.html',
                        context={'user': user, 'error': error})
        except Exception:
            return HttpResponseServerError("Echec du chargement de l'utilisateur")
    
    def post(self, request, id):
        try :
            username = request.POST["username"]
            password = request.POST["password"]

            if len(username) > 20 or len(password) > 20 or len(username) < 8 or len(password) < 8:
                return redirect(reverse('users_update', args=[id]) + f'?error=true')

            user = Users.objects.get(id=id)
            user.username = username
            user.password = password
            user.save()
            return redirect('users_list')
        except Exception:
            return HttpResponseServerError("Erreur 500 : Echec de la création de l'utilisateur");