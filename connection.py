# Importing Packages for SQL Connection
from sqlalchemy import create_engine, inspect
import sqlalchemy

# Importing Packages to Protect Info
import os
from dotenv import load_dotenv

# Importing Packages for Dataframe
from pandas import read_sql
import pandas as pd

load_dotenv()

DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

conn_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}'

db_engine = create_engine(conn_string, pool_pre_ping=True)
print (db_engine.table_names())

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM patients"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)
print(df)