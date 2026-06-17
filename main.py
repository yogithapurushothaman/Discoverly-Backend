from fastapi import FastAPI, Query
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
        "category": "Self Help",
    },
    {
        "id": 2,
        "name": "Rich Dad Poor Dad",
        "price": 399,
        "author": "Robert Kiyosaki",
        "category": "Finance",
    },
    {
        "id": 3,
        "name": "Think and Grow Rich",
        "price": 299,
        "author": "Napoleon Hill",
        "category": "Motivation",
    },
]

sellers = [
    {
        "id": 1,
        "name": "ABC Book Store",
        "location": "Chennai",
    },
    {
        "id": 2,
        "name": "Readers Hub",
        "location": "Coimbatore",
    },
    {
        "id": 3,
        "name": "Knowledge Mart",
        "location": "Madurai",
    },
]


@app.get("/")
def home():
    return {"message": "Welcome to Discoverly Backend!"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Discoverly Backend",
    }


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}


@app.get("/search")
def search_products(q: str = Query("")):
    return [
        product
        for product in products
        if q.lower() in product["name"].lower()
    ]


@app.get("/categories")
def get_categories():
    return [
        "Self Help",
        "Finance",
        "Motivation",
    ]


@app.get("/sellers")
def get_sellers():
    return sellers
wishlist = [
    {
        "id": 1,
        "name": "Atomic Habits",
    },
    {
        "id": 2,
        "name": "Rich Dad Poor Dad",
    },
]

@app.get("/wishlist")
def get_wishlist():
    return wishlist