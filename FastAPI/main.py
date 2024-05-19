from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, registry
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.future import select

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
    
class User1(Base):
    __tablename__ = 'SecondTable'
    
    name = Column(String, primary_key=True, index=True)
    address = Column(String)
    mobile = Column(Integer)
    
#------------------------------------------------------------------------------------Map Existing Table-------------
metadata = MetaData()


# Define the existing table structure
existing_table = Table(
    'APIFirstTable', metadata,
    Column('Name', String, primary_key=True),
    Column('Address', String),
    Column('mobile', Integer)
)

mapper_registry = registry()
@mapper_registry.mapped
class APIFirstTableModel:
    __table__ = existing_table



@app.get("/APITables/", tags=["APITables"])
async def read_data(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(APIFirstTableModel))
    items = result.scalars().all()
    return items

#-----------------------------------------------------------------------------------Map Existing Table ---------------
@app.get("/users/", tags=['FirstTable'])
async def read_items(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(User))
    items = result.scalars().all()
    return items


# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Example endpoint
@app.get("/users/", tags=['FirstTable'])
async def read_items(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(User))
    items = result.scalars().all()
    return items

@app.post("/users/", tags=['FirstTable'])
async def create_user(name: str, db: AsyncSession = Depends(get_db)):
    new_user = User(name=name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, session: AsyncSession = Depends(get_db)):
    item = await session.get(User, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    await session.commit()
    return {"message": "Item deleted successfully"}



@app.post("/users1/", tags=['SecondTable'])
async def create_user(name: str, db: AsyncSession = Depends(get_db)):
    new_user = User1(name=name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
    



# To test the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.1.1", port=8000)
