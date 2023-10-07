CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    admitted_date DATE
);

CREATE TABLE labs (
    lab_id INT PRIMARY KEY AUTO_INCREMENT,
    lab_name VARCHAR(100) NOT NULL
);

CREATE TABLE patient_lab (
    patient_lab_id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (lab_id) REFERENCES labs(lab_id)
);