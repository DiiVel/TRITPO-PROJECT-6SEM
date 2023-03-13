from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from config.database import get_db
from models.schemas import OrderCreatePlaceOrder
from order.orderservice import OrderService

router = APIRouter(prefix="/order", tags=["Order"])


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return OrderService.get_all(db=db)


@router.post("/")
def create_order(request: OrderCreatePlaceOrder, db: Session = Depends(get_db)):
    return OrderService.create_order_place(request=request, db=db)


@router.get("/orderbyuser/{userid}")
def order_by_user(userid: int, db: Session = Depends(get_db)):
    return OrderService.get_order_by_user_id(userid=userid, db=db)


@router.get("/orderbyid/{id}")
def order_by_id(id: int, db: Session = Depends(get_db)):
    return OrderService.get_order_by_id(id=id, db=db)

# @router.post("/create")
# def createOrder(request: OrderCreate, db: Session = Depends(get_db)):
#     return OrderService.createOrder(request=request, db=db)
