# Projet de gestion utilisateurs/équipes

## Installation 

1. Assurez vous d'avoir < python (3.10) > d'installé sur votre ordinateur ainsi que < pip > :
-> python : https://www.python.org/
-> pip : py get-pip.

2. Dans un répertoire clonez le git : https://github.com/justRB/django-project.git et modifiez *
le nom du dossier en "project"

3. Toujours dans le même répertoire créez un environnement virtuel et activez le
-> Créer l'environnement : python -m venv py310
-> (windows) Activez l'environnement : .\py310\Scripts\activate
-> (macOS/linux) Activez l'environnement : source py310\bin\activate

4. Votre répertoire parent contient maintenant le < dossier du projet > ainsi que le < dossier permettant l'activation 
de l'environnement virtuel >

5. Maintenant veillez à toujours être dans votre environnement virtuel, vous n'avez plus qu'à installer
les dépendances contenu dans le fichier requirements.txt dans le dossier du projet :
-> Installation des dépendances : pip install -r .\project\requirements.txt

6. Vous avez maintenant toutes les installations nécessaires, pour démarrer l'application utiliser
la commande suivante :
-> Démarrer l'application : python .\project\manage.py runserver

## Chemins d'url

1. Les urls passants par l'api ne nécessiteront pas d'authentifiation contrairement à celles
classiques par le web, voici un user de base pour vous connecter, sinon créez en un via l'api
-> Username : Alexander
-> Password : password

Url de base : app/

### USERS AUTH
-> LOGIN = login
-> LOGOUT = logout
-> HOME = home

### USERS API
-> GET ONE = api/users/view/{id} 
-> GET ALL = api/users/list
-> CREATE ONE = api/users/create
-> DELETE ONE = api/users/delete/{id}
-> UPDATE ONE = api/users/update/{id}
-> SHUFFLE TEAMS TO USERS = api/users/shuffle
-> RESET TEAMS TO USERS = api/users/reset

### TEAMS API
-> GET ONE = api/teams/view/{id}
-> GET ALL = api/teams/list 
-> CREATE ONE = api/teams/create 
-> DELETE ONE = api/teams/delete/{id} 
-> UPDATE ONE = api/teams/update/{id}

### USERS WEB
-> GET ALL = users/list
-> CREATE ONE = users/create
-> DELETE ONE = users/delete/{id}
-> UPDATE ONE = users/update/{id}
-> SHUFFLE TEAMS TO USERS = users/shuffle
-> RESET TEAMS TO USERS = users/reset

### TEAMS WEB
-> GET ALL = teams/list 
-> CREATE ONE = teams/create 
-> DELETE ONE = teams/delete/{id} 
-> UPDATE ONE = teams/update/{id}