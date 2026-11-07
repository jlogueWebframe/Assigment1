
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime

from db.connection import Base

class Contact(Base):
    """Require are not nullable."""
 
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(nullable=False,)
    first_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=True)
    address_line1: Mapped[str] = mapped_column(nullable=True)
    address_line2: Mapped[str] = mapped_column(nullable=True)
    province: Mapped[str] = mapped_column(nullable=True)
    postal_code: Mapped[str] = mapped_column(nullable=True)
    country: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

