from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL database URL
DATABASE_URL = "postgresql://jodos:jodos2006@localhost/nomad_track"  # Update as needed

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal class to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to use for models
Base = declarative_base()

# Function to get a database session for use in FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
