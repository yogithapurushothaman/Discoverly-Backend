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

products = [
    {
        "id": 1,
        "name": "Atomic Habits",
        "price": 499,
        "author": "James Clear",
    },
    {
        "id": 2,
        "name": "Rich Dad Poor Dad",
        "price": 399,
        "author": "Robert Kiyosaki",
    },
    {
        "id": 3,
        "name": "Think and Grow Rich",
        "price": 299,
        "author": "Napoleon Hill",
    },
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Discoverly Backend!"
    }


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }