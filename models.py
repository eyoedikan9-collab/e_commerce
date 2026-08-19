from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    pass

from database import engine
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]
    gender:  Mapped[str] = mapped_column(String(20))
    age: Mapped[int]
    hashed_password: Mapped[str]
    role: Mapped[str] = mapped_column(server_default="user")

    order: Mapped[List["Order"]] = relationship(back_populates="user")
    cart: Mapped["Cart"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, username={self.fullname!r}, gender={self.gender!r}, age={self.age!r})"
    
class Category(Base):
    __tablename__ = "categories"
    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(50))
   
    product: Mapped[List["Product"]] = relationship(back_populates="category")

    def __repr__(self) -> str:
        return f"Category(category_id={self.category_id!r}, name={self.name!r}, description={self.description!r})"

class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    category_id = mapped_column(ForeignKey("category.category_id"))
    price: Mapped[int]   
    description: Mapped[str] = mapped_column(String(50))
    stock_quantity: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(),nullable=False)


    cart_item: Mapped[List["CartItem"]] = relationship(back_populates="product")
    order_item: Mapped[List["OrderItem"]] = relationship(back_populates="product")
    category: Mapped["Category"] = relationship(back_populates="product")

    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, name={self.name!r}, category_id={self.category_id!r}, description={self.description!r}, price={self.price!r}, stock_quantity={self.stock_quantity!r}, created_at={self.created_at!r})"

class Cart(Base):
    __tablename__ = "carts"
    cart_id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.user_id"))

    cart_item: Mapped[List["CartItem"]] = relationship(back_populates="cart")
    user: Mapped["User"] = relationship(back_populates="cart")

    def __repr__(self) -> str:
        return f"Cart(cart_id={self.cart_id!r}, user_id={self.user_id!r})"

class CartItem(Base):
    __tablename__ = "cart_items"
    cartitem_id: Mapped[int] = mapped_column(primary_key=True)
    cart_id = mapped_column(ForeignKey("cart.cart_id"))
    product_id = mapped_column(ForeignKey("product.product_id"))
    quantity: Mapped[int]

    cart: Mapped["Cart"] = relationship(back_populates="cart_item")
    product: Mapped["Product"] = relationship(back_populates="cart_item")

    def __repr__(self) -> str:
        return f"CartItem(cartitem_id={self.cartitem_id!r}, cart_id={self.cart_id!r}, product_id={self.product_id!r}, quantity={self.quantity!r})"

class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    total_price: Mapped[int]
    user_id = mapped_column(ForeignKey("users.user_id"))
    status: Mapped[str] = mapped_column(server_default="pending") 
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(),nullable=False)


    user: Mapped["User"] = relationship(back_populates="order")
    order_item: Mapped[List["OrderItem"]] = relationship(back_populates="order")

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id!r}, total_price={self.total_price!r}, user_id={self.user_id!r}, status={self.status!r}, created_at={self.created_at!r})"


class OrderItem(Base):
    __tablename__ = "order_items"
    order_id = mapped_column(ForeignKey("order.order_id"))
    product_id = mapped_column(ForeignKey("product.product_id"))
    quantity: Mapped[int]
    price: Mapped[int]

    order: Mapped["Order"] = relationship(back_populates="order_item")
    product: Mapped["Product"] = relationship(back_populates="order_item")

    def __repr__(self) -> str:
        return f"OrderItem(orderitem_id={self.orderitem_id!r}, order_id={self.order_id!r}, product_id={self.product_id!r}, quantity={self.quantity!r}, price={self.price!r})"


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)



