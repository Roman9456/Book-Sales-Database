from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Database connection parameters
db_username = 'postgres'
db_password = ''
db_host = 'localhost'
db_name = 'declarative_base'

# Create a database engine
engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}")

try:
    # Try connecting to the database
    conn = engine.connect()
    conn.close()
    print("Database already exists.")
except OperationalError:
    # Create the database if it doesn't exist
    engine.execute(f"CREATE DATABASE {db_name}")
    print("Database created.")

engine.dispose()  # Close the engine
