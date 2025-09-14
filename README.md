# Appointment API - Flask & MySQL

## Project Setup and Installation Instructions

1. **Clone the Repository**

git clone https://github.com/purna1031/Hospital_Appointments.git
cd appointment-flask


2. **Create and Activate Virtual Environment**

python -m venv venv

Linux/Mac
source venv/bin/activate

Windows
venv\Scripts\activate


3. **Install Required Python Packages**

pip install flask mysql-connector-python


4. **Project Structure**

appointment-flask-api/
├── __pycache__
├── venv
├── app.py
├── config.py
├── requirements.txt
└── README.md


---

## MySQL Database Connection Instructions

1. **Create MySQL Database**

CREATE DATABASE appointments_flask;


2. **Create Appointments Table**

USE appointments_flask;

CREATE TABLE appointments (
id INT PRIMARY KEY AUTO_INCREMENT,
patient_name VARCHAR(100),
doctor_name VARCHAR(100),
appointment_date DATE,
appointment_time TIME,
purpose VARCHAR(255),
diagnosis TEXT,
prescription TEXT
);


3. **Configure Database Credentials**

Edit `config.py` with your MySQL settings:

MYSQL_CONFIG = {
'host': '127.0.0.1',
'user': 'your_mysql_username',
'password': 'your_mysql_password',
'database': 'appointments_flask',
'port': 3306
}


4. **Run the Flask Application**

python app.py


The API will be accessible at `http://127.0.0.1:5000/`.

---

## Testing the API

Use the provided Postman collection to test all CRUD endpoints for appointments including:

- GET all appointments
- GET appointment by ID
- POST create appointment
- PUT update appointment
- DELETE appointment

---


*This README is meant to guide setup, MySQL configuration, and API testing for the Appointment API project.*