# Employee Database and Feedback Application (CRUD)

## Introduction
This project is a **Python-based Employee Database and Feedback Application** that implements **CRUD operations**. It provides an interactive interface for managing employee records and collecting feedback, with distinct functionalities for **Admin and User roles**.

## Features Overview
The application consists of the following CRUD operations:

- **Create**: Adding new employee records and submitting feedback.
- **Read**: Viewing employee data and feedback.
- **Update**: Modifying employee details.
- **Delete**: Removing employee records.

## Roles & Functionalities

### 🔹 Admin Role
Admins have full control over employee and feedback data. The Admin menu includes:

- **Employee Database** – View all employee records and feedback.
- **Add Employee** – Enter new employee data.
- **Update Employee** – Modify existing employee details.
- **Delete Employee** – Remove an employee from the database.
- **Exit** – Logout from the Admin panel.

### 🔹 User Role
Users can submit feedback about the company. The User menu includes:

- **Employee Feedback Form** – Submit feedback with Employee ID.
- **Exit** – Logout from the User panel.

## Application Flow

### 🔹 Login System
- Users select their role (**Admin/User**) and enter credentials.
- Up to **3 login attempts** are allowed before the application exits.

### 🔹 Admin Operations
1. **Employee Database (Read Operation)**
   - Displays **Employee Table** and **Feedback Table**.
   - Includes **Search & Sort** functionalities.

2. **Add Employee (Create Operation)**
   - Admin inputs employee details.
   - Data validation and confirmation before saving.

3. **Update Employee (Update Operation)**
   - Admin selects an **Employee ID**.
   - Specific fields can be updated.
   - Confirmation and success message displayed.

4. **Delete Employee (Delete Operation)**
   - Admin selects an **Employee ID**.
   - Confirmation required before deletion.

### 🔹 User Operations
- **Submit Employee Feedback**
  - Users enter their **Employee ID**.
  - Fill out and submit a **feedback form**.

## 🛠️ Code Implementation
The system is built using **Python** and relies on:

- **PrettyTable** – For structured data presentation.
- **Datetime** – For managing timestamps.

## Key Functions
```python
def login():
    """Handles authentication."""
    pass

def admin():
    """Manages Admin menu."""
    pass

def user():
    """Manages User menu."""
    pass

def display_employee_database():
    """Reads and displays data."""
    pass

def add_employee():
    """Creates new employee records."""
    pass

def update_employee():
    """Modifies existing records."""
    pass

def delete_employee():
    """Removes employee records."""
    pass

def add_feedback():
    """Allows users to submit feedback."""
    pass
```
## Repository and Documentation

- Complete code and flowchart available on [Link](https://github.com/Chua-wd/Employee_Database_and_Feedback_Application_in_Python_-CRUD-/blob/main/M1_Capstone%20Project_Employee%20Database_Chua_Wira_Dirgantara.drawio.pdf)

- Article on [Medium](https://medium.com/@wiradirgantara55/employee-database-and-feedback-application-in-phyton-crud-c5f4204a21d6)

This project demonstrates a structured approach to handling employee records and feedback using CRUD operations in Python.
