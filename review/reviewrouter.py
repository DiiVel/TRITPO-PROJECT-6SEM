from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.db.models import User
from models.schemas import ReviewCreate
from config.token import get_current_user
from review.reviewservice import ReviewService

router = APIRouter(prefix="/review", tags=["Review"])


@router.get("/")
def get_all_review(db: Session = Depends(get_db)):
    return ReviewService.get_all(db=db)


@router.post("/create/{productid}")
def create_review(
    productid: int,
    request: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ReviewService.create_review(
        request=request, productId=productid, db=db, current_user=current_user
    )


@router.post("/coba")
def coba_review(request: ReviewCreate):
    return request
