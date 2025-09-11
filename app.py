from flask import Flask,request,jsonify
from config import MYSQL_CONFIG
import mysql.connector
import datetime
app=Flask(__name__)


def get_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)

# GET method

@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM appointments")
    results = cursor.fetchall()
    for row in results:
        for key, value in row.items():
            if isinstance(value, (datetime.date, datetime.datetime)):
                row[key] = value.isoformat()
            elif isinstance(value, datetime.timedelta):
                total_seconds = int(value.total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                row[key] = f"{hours:02}:{minutes:02}:{seconds:02}"
    cursor.close()
    conn.close()
    return jsonify(results), 200

@app.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM appointments WHERE id=%s", (id,))
    result = cursor.fetchone()

    if result is None:
        cursor.close()
        conn.close()
        return jsonify({"error": "Appointment not found"}), 404
    for key, value in result.items():
        if isinstance(value, (datetime.date, datetime.datetime)):
            result[key] = value.isoformat()
        elif isinstance(value, datetime.timedelta):
            total_seconds = int(value.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            result[key] = f"{hours:02}:{minutes:02}:{seconds:02}"
    cursor.close()
    conn.close()
    return jsonify(result), 200

#POST Method

@app.route("/appointments",methods=['POST'])
def create_appointment():
    data=request.json
    required = ['patient_name', 'doctor_name', 'appointment_date', 'appointment_time', 'purpose', 'diagnosis', 'prescription']
    if not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (patient_name, doctor_name, appointment_date, appointment_time, purpose, diagnosis, prescription)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,(data['patient_name'], data['doctor_name'], data['appointment_date'], data['appointment_time'], data['purpose'], data['diagnosis'], data['prescription']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Appointment created"}), 201


@app.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    data = request.json
    required = ['patient_name', 'doctor_name', 'appointment_date', 'appointment_time', 'purpose', 'diagnosis', 'prescription']
    if not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id=%s", (id,))
    if cursor.fetchone() is None:
        cursor.close()
        conn.close()
        return jsonify({"error": "Appointment not found"}), 404
    cursor.execute("""
        UPDATE appointments SET patient_name=%s, doctor_name=%s, appointment_date=%s,
        appointment_time=%s, purpose=%s, diagnosis=%s, prescription=%s WHERE id=%s
        """, (data['patient_name'], data['doctor_name'], data['appointment_date'], 
              data['appointment_time'], data['purpose'], data['diagnosis'], 
              data['prescription'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Appointment updated"}), 200

@app.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id=%s", (id,))
    if cursor.fetchone() is None:
        cursor.close()
        conn.close()
        return jsonify({"error": "Appointment not found"}), 404
    cursor.execute("DELETE FROM appointments WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Appointment deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
