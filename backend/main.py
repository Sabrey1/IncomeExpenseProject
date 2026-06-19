from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base

from app.routers import user, customer

import app.models.user, app.models.customer

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
app.include_router(customer.router, prefix="/customers", tags=["Customers"])


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}