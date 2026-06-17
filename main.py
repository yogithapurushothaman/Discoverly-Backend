from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Discoverly Backend!"
    }

@app.get("/products")
def get_products():
    return [
        {
            "id": 1,
            "name": "Atomic Habits",
            "price": 499
        },
        {
            "id": 2,
            "name": "Rich Dad Poor Dad",
            "price": 399
        },
        {
            "id": 3,
            "name": "Think and Grow Rich",
            "price": 299
        }
    ]