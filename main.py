from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample product data
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


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Discoverly Backend!"
    }


# Health Check API
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Discoverly Backend"
    }


# Get all products
@app.get("/products")
def get_products():
    return products


# Get a product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }


# Search products by name
@app.get("/search")
def search_products(q: str = Query("")):
    return [
        product
        for product in products
        if q.lower() in product["name"].lower()
    ]