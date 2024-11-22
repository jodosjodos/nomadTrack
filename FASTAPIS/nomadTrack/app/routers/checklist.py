from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import get_checklists,create_checklist 
from app.schemas import Checklist,ChecklistCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/checklists", response_model=list[Checklist])
def read_checklists(db: Session = Depends(get_db)):
    return get_checklists(db)

@router.post("/checklists", response_model=Checklist)
def create_checklist_req(checklist: ChecklistCreate, db: Session = Depends(get_db)):
    return create_checklist(db, checklist)  # Assuming user_id=1
