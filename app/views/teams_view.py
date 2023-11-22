from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseServerError
from django.views import View
from app.models import Teams

# READ
class TeamsList(View):
    def get(self, request):
        try:
            teams = Teams.objects.all()
            return render(request, template_name='teams/teams_list.html',
                          context={'teams': teams})
        except Exception:
            return HttpResponseServerError("Impossible de charger la liste d'équipes")
        
# CREATE
class TeamsCreate(View):
    def get(selft, request):
        error = request.GET.get('error', False)
        return render(request, template_name='teams/teams_create.html',
                      context={'error': error})
    
    def post(self, request):
        try:
            name = request.POST["name"]

            if len(name) > 20 or len(name) < 8:
                return redirect(reverse('teams_create') + f'?error=true')
            
            team = Teams.objects.create(name=name)
            team.save()
            return redirect('teams_list')
        except Exception:
            return HttpResponseServerError("Echec de la création de l'équipe")

# DELETE
class TeamsDelete(View):
    def get(self, request, id):
        try:
            team = Teams.objects.get(id=id)
            team.delete()
            return redirect('teams_list')
        except Exception:
            return HttpResponseServerError("Echec de la suppression de l'équipe")

# UPDATE
class TeamsUpdate(View):
    def get(self, request, id):
        error = request.GET.get('error', False)
        try:
            team = Teams.objects.get(id=id)
            return render(request, template_name='teams/teams_update.html',
                          context={'team': team, 'error': error})
        except Exception:
            return HttpResponseServerError("Echec du chargement de l'équipe")

    def post(self, request, id):
        try:
            name = request.POST["name"]

            if len(name) > 20 or len(name) < 8:
                return redirect(reverse('teams_update', args=[id]) + f'?error=true')      
            
            team = Teams.objects.get(id=id)
            team.name = name
            team.save()
            return redirect('teams_list')
        except Exception:
            return HttpResponseServerError("Echec de la modification de l'équipe")