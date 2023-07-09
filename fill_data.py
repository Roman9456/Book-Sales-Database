import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Publisher, Book, Shop, Stock, Sale

# Database connection parameters
db_username = 'postgres'
db_password = ''
db_host = 'localhost'
db_port = '5432'
db_name = 'declarative_base'

# Construct the connection string
connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create a database engine
engine = create_engine(connection_string)

# Create tables based on model definitions
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read test data from JSON file
with open('tests_data.json') as f:
    test_data = json.load(f)

# Map model names to their corresponding classes
model_mapping = {
    'publisher': Publisher,
    'book': Book,
    'shop': Shop,
    'stock': Stock,
    'sale': Sale
}

# Iterate over the test data and create model instances
for item in test_data:
    model_name = item['model']
    model_class = model_mapping.get(model_name)

    if model_class:
        fields = item['fields']
        model_instance = model_class(**fields)
        session.add(model_instance)

# Commit the changes to the database
session.commit()

# Close the session
session.close()



