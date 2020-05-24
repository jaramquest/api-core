from fastapi import FastAPI
from fastalchemy import SQLAlchemyMiddleware, db

from . import database, models

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware,
                   db_module=database,
                   models_module=models)

from .models import User
from . import schemas


@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    user = User(name=user.name, id=user.id, email=user.email)
    db.add(user)
    db.commit()
    return user


@app.get('/users')
def get_users():
    '''Return users.'''
    users = db.query(User).order_by(User.id).all()
    return users