import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker
import random

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

conn_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}'

db_engine = create_engine(conn_string, pool_pre_ping=True)
fake = Faker()

# Creating fake data

sample_labs = ['CBC', 'Urinanalysis', 'Lipid Panel', 'Basic Metabolic Panel', 'Comprehensive Metabolic Panel', 'Thyroid Test', 'hCG Test', 'LFT']
def insert_fake_data(engine, num_patients=200, num_labs=75, num_patient_lab=150):
    with engine.connect() as connection:
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=5, maximum_age=100)
            admitted_date = fake.admitted_date()
            connection.execute(f"INSERT INTO patients (first_name, last_name, date_of_birth, admitted_date) VALUES ('{first_name}', '{last_name}', '{date_of_birth}', '{admitted_date})")

        for labs in sample_labs:
            connection.execute(f"INSERT INTO labs (lab_name) VALUES ('{labs}')") #
        
        patient_id = [row[0] for row in connection.execute("SELECT patient_id FROM patients").fetchall()] 
        lab_id = [row[0] for row in connection.execute("SELECT lab_id FROM labs").fetchall()]
        
        for _ in range(num_patient_lab):
            patient_id = random.choice(patient_id)
            lab_id = random.choice(lab_id)
            connection.execute(f"""INSERT INTO patient_lab (patient_id, lab_id) VALUES ({patient_id}, {lab_id})""")

if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Imported fake data")