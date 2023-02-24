from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

#models
class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float]

    def __repr__(self) -> str:
        return '{id:%s, name:%s, price: %s}' % (self.id, self.name, self.price)
