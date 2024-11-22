from fastapi import FastAPI
from app.database import engine, Base
from app.routers import travel, checklist, users

app = FastAPI()

# Ensure models are registered with Base
from app.models import Travel, Checklist, User  # Import your models

# Create database tables (this will only create new tables, not update existing ones)
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(travel.router, prefix="/api", tags=["travels"])
app.include_router(checklist.router, prefix="/api", tags=["checklists"])
app.include_router(users.router, prefix="/api", tags=["users"])  # Register the user router
