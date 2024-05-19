from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models
from .main import SessionLocal, engine, app
from pydantic import BaseModel
import uvicorn

models.Base.metadata.create_all(bind=engine)

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(SessionLocal)):
    db_user = models.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/")
async def read_root(limit, published:bool):
    if published:
        return {'message':f'limit is {limit}, and published is {published}'}
    else:
        return {'message':f'limit is {limit}, and published is false {published}'}

@app.get('/about')
async def about():
    return {'data':{'message':'About'}}

class samplemodel(BaseModel):
    name : str
    age : int
    desc : str
    pass

@app.post('/create')
async def createpost(samplemodel : samplemodel):
    return {'message':f'post Created {samplemodel.name}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.1.1', port=9000)