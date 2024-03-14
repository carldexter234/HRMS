import mysql.connector
import os
import datetime

# Establish connection to MySQL HRMS database
conn_hrms = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database='sql_hr'  
)

cursor_hrms = conn_hrms.cursor()

# Function to record employee time in
def time_in_employee(employee_id):
    now = datetime.datetime.now()
    time_in = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor_hrms.execute('''INSERT INTO time_logs (employee_id, time_in) VALUES (%s, %s)''', (employee_id, time_in))
    conn_hrms.commit()

# Function to record employee time out
def time_out_employee(employee_id):
    now = datetime.datetime.now()
    time_out = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor_hrms.execute('''UPDATE time_logs SET time_out = %s WHERE employee_id = %s AND time_out IS NULL''', (time_out, employee_id))
    conn_hrms.commit()

# Function to approve or reject a leave request in HRMS
def manage_leave_request(request_id, status):
    cursor_hrms.execute('''UPDATE leave_requests SET status = %s WHERE id = %s''', (status, request_id))
    conn_hrms.commit()

# Function to view all leave requests in HRMS
def view_all_leave_requests_hrms():
    cursor_hrms.execute('''SELECT * FROM leave_requests''')
    requests = cursor_hrms.fetchall()
    for req in requests:
        print(req)

# Function to delete an employee in HRMS
def delete_employee_hrms(employee_id):
    cursor_hrms.execute('''DELETE FROM employees WHERE id = %s''', (employee_id,))
    conn_hrms.commit()

# Function to update an employee's information in HRMS
def update_employee_hrms(employee_id, name, department, position, salary, hire_date):
    cursor_hrms.execute('''UPDATE employees SET name = %s, department = %s, position = %s, salary = %s, hire_date = %s WHERE id = %s''',
                    (name, department, position, salary, hire_date, employee_id))
    conn_hrms.commit()

# Close the connection to HRMS database when done
def close_hrms_connection():
    conn_hrms.close()
