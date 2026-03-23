from fastapi import FastAPI
import models
from database import moteur, Base
from route import router as article_router

models.Base.metadata.create_all(bind=moteur)
app = FastAPI(title="MON API BACKEND",description="API pour un blog avec gestion des articles",version="1.0.0")
app.include_router(article_router)
@app.get("/")
def root():
    return {"message": "L'API est en ligne, Allez sur http://127.0.0.1:8000/docs  pour tester."}
