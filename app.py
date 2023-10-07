from flask import Flask, render_template
from pandas import read_sql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
import sqlalchemy

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}"
    "?charset=utf8mb4"
)

# Database connection settings
db_engine = create_engine(conn_string, pool_pre_ping=True)

@app.route('/')
def index():
    query_patients = "SELECT * FROM patient"
    df_patients = read_sql(query_patients, db_engine)
    data_patients = df_patients.to_dict(orient='records')

    query_labs = "SELECT * FROM labs"
    df_labs = read_sql(query_labs, db_engine)
    data_labs = df_labs.to_dict(orient='records')

    query_patient_labs = "SELECT * FROM patient_labs"
    df_patient_labs= read_sql(query_patient_labs, db_engine)
    data_patient_labs = df_patient_labs.to_dict(orient='records')

    return render_template('index.html', data_patients=data_patients, data_labs=data_labs, data_patient_labs=data_patient_labs)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=3306
        )
