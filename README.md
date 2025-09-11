# 🏥 Hospital Appointments System

A **Flask** web application to manage hospital appointments with a **MySQL database**.

---

## 🚀 Project Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/purna1031/Hospital_Appointments.git
cd Hospital_Appointments
### 2. Create a Virtual Environment
  python -m venv venv
  venv\Scripts\activate   # On Windows
  # OR
  source venv/bin/activate   # On Linux/Mac
### 3. Install Dependencies
  pip install flask flask-mysql-connector
### 4. Run the Flask App
  python app.py


## 🛠️ MySQL Database Connection Setup
### 1. Create a Database

  Open MySQL shell:
  CREATE DATABASE hospital_db;

### 2. Update Connection in app.py (or config.py)
  from flask import Flask
  from flask_mysql_connector import MySQL

  app = Flask(__name__)
  app.config['MYSQL_HOST'] = 'localhost'
  app.config['MYSQL_USER'] = 'root'
  app.config['MYSQL_PASSWORD'] = 'yourpassword'
  app.config['MYSQL_DATABASE'] = 'hospital_db'
  mysql = MySQL(app)

  Replace root with your MySQL username
  Replace yourpassword with your MySQL password

## 🗄️ SQL Schema (Copy & Run in MySQL)

  USE hospital_db;
  CREATE TABLE appointments (
      appointmentsid INT AUTO_INCREMENT PRIMARY KEY,
      patient_name VARCHAR(100) NOT NULL,
      doctor_name VARCHAR(100) NOT NULL,
      appointment_date DATE NOT NULL,
      appointment_time TIME NOT NULL,
      purpose VARCHAR(255),
      diagnosis TEXT,
      prescription TEXT
  );
