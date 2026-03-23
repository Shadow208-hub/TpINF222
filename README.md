# TpINF222
Développement des API backend 
Blog API - Backend (FastAPI)Une API RESTful robuste pour la gestion d'articles de blog, construite avec Python et FastAPI. Ce projet a été concu pour offrir une gestion complete du cycle de vie des articles (CRUD) avec une base de donnees relationnelle.
Fonctionnalit:
Gestion des Articles : Creation, lecture, mise à jour et suppression (CRUD).    
Validation des Donnees : Utilisation de Pydantic v1 pour assurer l'intégrité des donnees entrantes et sortantes.    
Base de Donnees : Integration de SQLAlchemy avec une base de donnees SQLite locale (.blog.db).    Documentation Automatique : Acces interactif aux points de terminaison via Swagger UI et ReDoc.
 Stack Technique  
 Framework : FastAPI   
 ORM : SQLAlchemy   
 Validation : Pydantic v1    
 Base de donnees : SQLite    
 Serveur ASGI : Uvicorn
 Structure du Projet
main.py          # Point d'entree de l'application et configuration FastAPI 
models.py        # Definition des modeles de base de donnees (SQLAlchemy)
schemas.py       # Schemas de validation et de reponse (Pydantic)
route.py         # Definition des routes et de la logique metier
database.py      # Configuration de la session et de la connexion DB
.blog.db         # Base de donnees SQLite (généré au premier lancement)

Installation et Lancement    Cloner le depott :    Bash  :git clone https://github.com/Shadow208-hub/TpINF222
Creer un environnement virtuel :
Bash :python -m venv venvsource venv/bin/activate 
Installer les dependances :Bash
pip install fastapi uvicorn sqlalchemy pydantic==1.10.12
Lancer le serveur :Bash   
uvicorn main:app 
L'API sera disponible sur : http://127.0.0.1:8000
Utilisation (Documentation)Une fois le serveur lancé, vous pouvez tester l'API directement via les interfaces de documentation automatique fournies par FastAPI : http://127.0.0.1:8000/docs  
Swagger UI :    ReDoc : http://127.0.0.1:8000/redoc
Exemples de Points de Terminaisons
methode,Route,Description
POST,/articles/,Creer un nouvel article
GET,/articles/,Lister tous les articles (avec pagination)
GET,/articles/{id}, Récupérer un article par son identifiant unique
PUT,/articles/{id},Modifier partiellement ou totalement un article
DELETE,/articles/{id},Supprimer definitivement un article
