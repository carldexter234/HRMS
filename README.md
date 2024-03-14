
# Python HRMS (Human Resource Management System)

This Python HRMS (Human Resource Management System) is designed to facilitate various HR-related tasks such as employee time tracking, leave management, and employee data management. It integrates with a MySQL database for data storage.

## Features

- **Leave Management:** Approve or reject leave requests submitted by employees.
- **Employee Data Management:** Update employee information such as name, department, position, salary, and hire date.
- **Time Tracking:** Track employee time in and time out to monitor attendance and working hours.

## How to Use

1. Ensure you have Python installed on your system.
2. Set up a MySQL database and configure the connection details in the code.
3. Run the Python script to execute the desired HRMS functions.

## Requirements

- Python 3.x
- MySQL
- `mysql-connector-python` library

## Installation

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Configure the MySQL connection details in the code.
4. Run the Python script to start using the HRMS.

## Sample Usage

```python
# Example usage of HRMS functions
import hrms

# Approve a leave request
hrms.manage_leave_request(request_id, "Approved")

# Update employee information
hrms.update_employee_hrms(employee_id, "John Doe", "HR", "Manager", 50000, "2024-01-01")

# View all leave requests
hrms.view_all_leave_requests_hrms()

# Close the HRMS connection
hrms.close_hrms_connection()



