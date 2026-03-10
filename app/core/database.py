from sqlmodel import SQLModel, Session, create_engine

# SQLite database file path
sqlite_file_name = "nexus_intel.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False is needed in SQLite to allow multiple threads to interact 
# with the database (essential for web frameworks like FastAPI)
connect_args = {"check_same_thread": False}

# Create the engine
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    """Creates the database and all tables defined in SQLModel metadata."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency generator for providing a database session."""
    with Session(engine) as session:
        yield session