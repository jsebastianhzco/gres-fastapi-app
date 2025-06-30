from fastapi import FastAPI
from app.database import Base, engine
from app.routers import cliente

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(cliente.router)
