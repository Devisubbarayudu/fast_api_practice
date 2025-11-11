from fastapi import FastAPI

app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Tablet", "price": 299.99},
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/products")
def get_products():
    return  products






# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)