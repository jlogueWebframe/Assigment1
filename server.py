from fastapi import FastAPI, Depends, HTTPException, status, Response, Query, Path

from sqlalchemy.orm import Session

from db.connection import get_db
from db.models import Contact
from db.schemas import ContactCreate,  ContactBase, ContactRead, ContactUpdate

app = FastAPI(title= "Contacts API", version="1.0.0", description="A simple API for managing Contacts.")

@app.get("/api/contacts", response_model=list[ContactRead], description="Retrieves all contacts from the database.")
def list_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@app.get("/api/contacts/last_name", response_model=list[ContactRead], description="Retrieves contacts filtered by last name.")
def list_contacts(last_name: str | None = Query(default=None, min_length=1, max_length=50), db: Session = Depends(get_db)):
    contacts = db.query(Contact)
    if last_name is not None:
        contacts = contacts.filter(Contact.last_name == last_name)
    return contacts.all()




@app.post("/api/contacts", 
          response_model=ContactRead, 
          description="Creates a new contact in the database.",
          status_code=status.HTTP_201_CREATED)
def create_contact( payload: ContactCreate,db: Session = Depends(get_db)) -> Contact:
    new_contact = Contact(**payload.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@app.put("/api/contacts/{contact_id}",
         response_model=ContactRead,
         description="Updates an existing contact by ID.")
def update_contact(contact_id: int, payload: ContactUpdate, db: Session = Depends(get_db)) -> Contact:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found.")

    for field, value in payload.model_dump().items():
        setattr(contact, field, value)

    db.commit()
    db.refresh(contact)
    return contact

@app.delete("/api/contacts/{contact_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response,
            description="Deletes a contact from the database.")
def delete_contact(
    contact_id: int = Path(description="ID value of the contact to be deleted"),
    db: Session = Depends(get_db),
) -> Response:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found.")

    db.delete(contact)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
