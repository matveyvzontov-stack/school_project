from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.note.NoteResponse)
def create_note(note: schemas.note.NoteCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=note.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found. Cannot create note.")
    return crud.create_note(db=db, note=note)

@router.get("/", response_model=List[schemas.note.NoteResponse])
def read_notes(user_id: int, db: Session = Depends(get_db)):
    return crud.get_notes_by_user(db, user_id=user_id)

@router.get("/{note_id}", response_model=schemas.note.NoteResponse)
def read_note_details(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note_by_id(db, note_id=note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.put("/{note_id}", response_model=schemas.note.NoteResponse)
def modify_note(note_id: int, note_update: schemas.note.NoteUpdate, db: Session = Depends(get_db)):
    db_note = crud.update_note(db, note_id=note_id, note_update=note_update)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}")
def remove_note(note_id: int, db: Session = Depends(get_db)):
    success = crud.delete_note(db, note_id=note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
