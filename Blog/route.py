from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Article
from datetime import datetime
from schemas import ArticleCreate,ArticleUpdate,ArticleResponse

router = APIRouter(prefix="/articles", tags=["articles"])
@router.post("/",response_model=ArticleResponse, status_code= status.HTTP_201_CREATED)
def create_article(article:ArticleCreate, db: Session =Depends(get_db)):
    new_article = Article(**article.dict())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

@router.get("/",response_model=List[ArticleResponse],status_code=status.HTTP_200_OK)
def get_article(skip: int=0, limit=100, db: Session = Depends(get_db)):
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles

@router.get("/{article_id}",response_model=ArticleResponse)
def search_article(article_id: int, db: Session = Depends(get_db)):
    search = db.query(Article).filter(Article.id==article_id).first()
    if not article_id:
        raise HTTPException(status_code=404, detail="Article no trouve")
    return search
    
@router.put("/{article_id}",response_model=ArticleResponse)
def update_article(article_id: int, article: ArticleUpdate,db: Session = Depends(get_db)):
    update= db.query(Article).filter(Article.id==article_id).first()
    if not update:
        raise HTTPException(status_code=404, detail="Article non trouve")
    
    update_data = article.dict(exclude_unset=True)
    for field , value in update_data.items():
        setattr(update, field,value)
        
    db.commit()
    db.refresh(update)
    return update

@router.delete("/{article_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    delete_data = db.query(Article).filter(Article.id==article_id).first()
    if not delete_data:
        raise HTTPException(status_code=404, detail="Article non trouve")
    db.delete(delete_data)
    db.commit()
    return None
    
@router.get("search/title/{article_title}",response_model=List[ArticleResponse])
def parametr_search(article_title: str, db: Session = Depends(get_db)):
    search_data = db.query(Article).filter(Article.title==article_title).all()
    if not search_data:
        raise HTTPException(status_code=404, detail="Article no trouve")
    return search_data

@router.get("search/date/{article_date}", response_model=List[ArticleResponse])
def date_search(article_date: datetime, db: Session = Depends(get_db)):
    date_data = db.query(Article).filter(Article.created_at == article_date).all()
    return date_data

@router.get("search/content/{article_content}", response_model=List[ArticleResponse])
def content_search(article_content: str, db: Session = Depends(get_db)):
    content = db.query(Article).filter(Article.content == article_content).all()
    return content
    
