from sqlalchemy.orm import Session
from app.models import Checklist, Travel, Checking
from app.schemas import ChecklistCreate, TravelCreate


# Checklist CRUD
def get_checklists(db: Session):
    return db.query(Checklist).all()


def create_checklist(db: Session, checklist: ChecklistCreate):
    db_checklist = Checklist(**checklist.dict())
    db.add(db_checklist)
    db.commit()
    db.refresh(db_checklist)
    return db_checklist


# Travel CRUD
def get_travels(db: Session):
    return db.query(Travel).all()


def create_travel(db: Session, travel: TravelCreate):
    db_travel = Travel(**travel.dict(exclude={"checklist_ids"}))
    db_checklists = (
        db.query(Checklist).filter(Checklist.id.in_(travel.checklist_ids)).all()
    )
    db_travel.checklists.extend(db_checklists)
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel


from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

# Initialize password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Function to hash the password before storing it in the database
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Function to create a new user
def create_user(db: Session, user: UserCreate):
    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create the user instance
    db_user = User(username=user.username, email=user.email, password=hashed_password)

    # Add the new user to the session
    db.add(db_user)

    # Commit the transaction and flush the session
    try:
        db.commit()  # Commit the transaction to the database
        db.refresh(db_user)  # Refresh the instance to reflect the committed changes
        return db_user
    except IntegrityError:
        db.rollback()  # Rollback if any IntegrityError occurs (e.g., duplicate email/username)
        raise ValueError("Username or email already exists.")
    except Exception as e:
        db.rollback()  # Rollback in case of any other errors
        raise e  # Raise the exception to be handled elsewhere


# Function to get all users
def get_all_users(db: Session):
    # Query all users from the database
    users = db.query(User).all()
    return users
