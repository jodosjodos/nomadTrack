from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import get_travels, create_travel
from app.schemas import Travel, TravelCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/travels", response_model=list[Travel])
def read_travels(db: Session = Depends(get_db)):
    return get_travels(db)

@router.post("/travels", response_model=Travel)
def create_travel_req(travel: TravelCreate, db: Session = Depends(get_db)):
    return create_travel(db, travel)  # Assuming user_id=1
