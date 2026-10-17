from fastapi import APIRouter, HTTPException

from .. import storage
from ..schemas import Product

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
def get_products(limit: int = 10):
    return list(storage.products.values())[:limit]


@router.get("/{product_id}")
def get_product(product_id: int):
    product = storage.products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return product


@router.post("/", status_code=201)
def crear_producto(product: Product):

    product.id = storage.nuevo_id
    storage.products[storage.nuevo_id] = product
    storage.nuevo_id += 1

    return product


@router.delete("/{product_id}")
def eliminar_product(product_id: int):
    product = storage.products.pop(product_id, None)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="producto no encontrado",
        )
    return product
