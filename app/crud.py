from sqlalchemy.orm import Session
from app.models import User, Note
from app.schemas.user import UserCreate
from app.schemas.note import NoteCreate, NoteUpdate

### 👤 User CRUD Helpers
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password + "_fake_hash"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

### 📝 Notes CRUD Helpers
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

def get_notes_by_user(db: Session, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        user_id=note.user_id,
        title=note.title,
        content=note.content
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note_update: NoteUpdate):
    db_note = get_note_by_id(db, note_id)
    if not db_note:
        return None
    if note_update.title is not None:
        db_note.title = note_update.title
    if note_update.content is not None:
        db_note.content = note_update.content
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note_by_id(db, note_id)
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    return False
