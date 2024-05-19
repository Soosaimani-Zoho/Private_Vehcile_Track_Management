from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/fastAPI"

# SQLAlchemy setup
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

# Create FastAPI app
app = FastAPI()

# Dependency to get DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

# Example model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class APIFirstTables(Base):
    __tablename__ = 'APIFirstTable'
    name = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    mobile = Column(Integer, unique=True, index=True)

# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Example endpoint
@app.post("/users/", tags=['UserTable'])
async def create_user(name: str, db: AsyncSession = Depends(get_db)):
    new_user = User(name=name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.post("/mysqltable/", tags=['mysqltable'])
async def create(APIFirstTable: APIFirstTables, db: AsyncSession = Depends(get_db)):
    new_user = User(name=APIFirstTable.name,address = APIFirstTable.address, mobile=APIFirstTable.mobile)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user.name


# To test the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.1.1", port=8000)
