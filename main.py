from fastapi import FastAPI
from models import Product
from cofig import session, engine
import db_models

app = FastAPI()

db_models.Base.metadata.create_all(bind = engine)

products = [
    Product(id=1, name = "Phone", description = "budget phone", price=99, quantity=10),
    Product(id=2, name = "laptop", description = "gaming laptop", price=999, quantity=5),
    Product(id=5, name ="headphones", description ="wireless headphones", price=9, quantity=15)

]


@app.get("/products")
def all_products():
    db = session()
    db.query()
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Product Not found"


@app.post ("/products")
def add_products(product:Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return " Product Added Successfully"
    return "Product Not found"


@app.delete("/product")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return " Product Not found"
