from fastapi import Depends
from models.db.models import ProductModel

from config.token import get_current_user
from models.db.models import ReviewModel

from models.db.models import User
from config.database import get_db
from sqlalchemy.orm import Session
from models.schemas import ReviewCreate


class ReviewService:
    def get_all(db: Session):
        return db.query(ReviewModel).all()

    def create_review(
            request: ReviewCreate,
            productId: int,
            db: Session = Depends(get_db),
            current_user: User = Depends(get_current_user),
    ):
        product_byid = (
            db.query(ProductModel).filter(ProductModel.id == productId).first()
        )

        try:

            review_new = ReviewModel(
                name=current_user.name,
                user_id=current_user.id,
                rating=request.rating,
                comment=request.comment,
            )
            review_new.product_id = product_byid.id

            db.add(review_new)
            db.commit()
        except Exception as e:
            return e

        return "Yahshasha"
