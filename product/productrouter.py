from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas import ProductSchema
from config.database import get_db

from product.productservice import ProductService

router = APIRouter(prefix="/product", tags=["Products"])


@router.get("/")
def get_all_product(db: Session = Depends(get_db)):
    return ProductService.get_all_product(db=db)


@router.post("/")
def create_product(request: ProductSchema, db: Session = Depends(get_db)):
    return ProductService.create_product(request=request, db=db)


@router.get("/{productid}")
def show_product(productid: int, db: Session = Depends(get_db)):
    return ProductService.show_product(productid=productid, db=db)


@router.put("/{productid}")
def update_product(
    productid: int, request: ProductSchema, db: Session = Depends(get_db)
):
    return ProductService.update_product(productid=productid, request=request, db=db)


@router.delete("/{productid}")
def delete_product(productid: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(productid=productid, db=db)
