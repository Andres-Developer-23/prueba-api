from fastapi import FastAPI

from .routes.products import router as products_routers

app = FastAPI()

app.include_router(products_routers)

@app.get("/")
def home():
    return {"mensaje": "Hola mundo"}
