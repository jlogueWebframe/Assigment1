from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field

class ContactBase(BaseModel):
    email_address: str = Field(min_length=5, max_length=100)
    first_name: str = Field(min_length=1, max_length=50)
    middle_name: str | None = Field(default=None, min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    phone: str | None = Field(default=None, min_length=7, max_length=15)
    address_line1: str | None = Field(default=None, min_length=1, max_length=100)
    address_line2: str | None = Field(default=None, min_length=1, max_length=100)
    province: str | None = Field(default=None, min_length=1, max_length=50)
    postal_code: str | None = Field(default=None, min_length=3, max_length=10)
    country: str | None = Field(default=None, min_length=2, max_length=50)


class ContactCreate(ContactBase):
    """Validates the body of POST /api/contacts/."""

class ContactRead(ContactBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime


class ContactUpdate(ContactBase):
    """Validates the complete replacement body of PUT /api/contacts/{id}."""

