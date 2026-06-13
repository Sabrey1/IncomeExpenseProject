from fastapi import FastAPI
from database import engine, Base
import model
from app.routers import user
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}