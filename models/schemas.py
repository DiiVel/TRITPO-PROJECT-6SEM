from pydantic import BaseModel
from typing import List, Optional


class CartSchema(BaseModel):
    address_line1: str
    address_city: str
    address_country: str
    address_zip: str


class TokenSchema(BaseModel):
    id: str
    email: str
    card: CartSchema


class CartItemSchema(BaseModel):
    name: str
    quantity: int
    price: int


class CurrentUserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_staff: bool
    is_active: bool


class OrderCreatePlaceOrder(BaseModel):
    token: TokenSchema
    cartItems: List[CartItemSchema]
    currentUser: CurrentUserSchema
    subtotal: int


class ReviewSchema(BaseModel):
    user_id: int
    name: str
    comment: str
    rating: int


class ProductSchema(BaseModel):
    name: str
    image: str
    category: str
    description: str
    price: int
    countInStock: int
    rating: Optional[int]


class ReviewCreate(BaseModel):
    rating: int
    comment: str


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]
