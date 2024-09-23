# Libraries
from prettytable import PrettyTable
from datetime import datetime

#Dummy Database
admin_credentials = {'admin': 'myadmin'}

employee_table = PrettyTable()

employee_id = "Employee_Id"
employee_name = "Employee_Name"
birthdate = "Birthdate"
joining_date = "Joining_Date"
department = "Department"
job = "Job"
position = "Position"
salary = "Salary"
employment_status = "Employment_Status"
region = "Region"

employee_table.field_names = [employee_id, employee_name, birthdate, joining_date, department, job, position, salary, employment_status, region]

employee_table.align[employee_name] = "l"
employee_table.align[birthdate] = "r"
employee_table.align[joining_date] = "r"
employee_table.align[department] = "l"
employee_table.align[job] = "l"
employee_table.align[position] = "l"
employee_table.align[salary] = "r"
employee_table.align[employment_status] = "l"
employee_table.align[region] = "l"

employee_table.add_row(["ED20190501", "John Haryanto", datetime.strptime("1997-05-12", "%Y-%m-%d").date(), datetime.strptime("2019-08-01", "%Y-%m-%d").date(), "Tech Support", "Support Specialist", "Senior-level", 12000000, "Full-Time", "Jakarta"])
employee_table.add_row(["ED20180302", "Lisa Tanaka", datetime.strptime("1992-11-30", "%Y-%m-%d").date(), datetime.strptime("2018-03-15", "%Y-%m-%d").date(), "Marketing", "Digital Marketer", "Managerial-level", 12000000, "Full-Time", "Bandung"])
employee_table.add_row(["ED20200703", "Ravi Kumar", datetime.strptime("1995-01-23", "%Y-%m-%d").date(), datetime.strptime("2020-07-20", "%Y-%m-%d").date(), "Product Development", "Product Manager", "Managerial-level", 13000000, "Full-Time", "Surabaya"])
employee_table.add_row(["ED20160204", "Maria Andini", datetime.strptime("1989-09-16", "%Y-%m-%d").date(), datetime.strptime("2016-02-10", "%Y-%m-%d").date(), "Data Analysis", "Data Scientist", "Senior-level", 11500000, "Full-Time", "Yogyakarta"])
employee_table.add_row(["ED20230105", "Ethan Jones", datetime.strptime("2000-02-10", "%Y-%m-%d").date(), datetime.strptime("2023-01-01", "%Y-%m-%d").date(), "Customer Service", "Customer Support", "Entry-level", 5000000, "Part-Time", "Medan"])
employee_table.add_row(["ED20170606", "Ayu Putri", datetime.strptime("1994-04-07", "%Y-%m-%d").date(), datetime.strptime("2017-06-25", "%Y-%m-%d").date(), "HR", "HR Manager", "Managerial-level", 12500000, "Full-Time", "Jakarta"])
employee_table.add_row(["ED20220907", "Samuel Robinson", datetime.strptime("1998-10-30", "%Y-%m-%d").date(), datetime.strptime("2022-09-01", "%Y-%m-%d").date(), "Sales", "Sales Executive", "Senior-level", 11000000, "Full-Time", "Bandung"])
employee_table.add_row(["ED20151108", "Tariq Basir", datetime.strptime("1993-03-14", "%Y-%m-%d").date(), datetime.strptime("2015-11-20", "%Y-%m-%d").date(), "Logistics", "Logistics Coordinator", "Intermediate", 7500000, "Full-Time", "Surabaya"])
employee_table.add_row(["ED20240309", "Nina Zhang", datetime.strptime("2001-07-21", "%Y-%m-%d").date(), datetime.strptime("2024-03-01", "%Y-%m-%d").date(), "UX/UI Design", "UI Designer", "Entry-level", 6000000, "Part-Time", "Yogyakarta"])
employee_table.add_row(["ED20141010", "Daniella Herrera", datetime.strptime("1988-12-05", "%Y-%m-%d").date(), datetime.strptime("2014-10-15", "%Y-%m-%d").date(), "Finance", "Finance Analyst", "Senior-level", 10500000, "Full-Time", "Medan"])
employee_table.add_row(["ED20230301", "Michael Lee", datetime.strptime("1990-03-12", "%Y-%m-%d").date(), datetime.strptime("2023-03-01", "%Y-%m-%d").date(), "IT Support", "IT Technician", "Intermediate", 12000000, "Full-Time", "Jakarta"])
employee_table.add_row(["ED20230402", "Sophia Chen", datetime.strptime("1985-07-18", "%Y-%m-%d").date(), datetime.strptime("2023-04-02", "%Y-%m-%d").date(), "Marketing", "Marketing Specialist", "Intermediate", 8000000, "Full-Time", "Bandung"])
employee_table.add_row(["ED20230503", "Liam Johnson", datetime.strptime("1993-09-25", "%Y-%m-%d").date(), datetime.strptime("2023-05-03", "%Y-%m-%d").date(), "Sales", "Sales Manager", "Senior-level", 9000000, "Full-Time", "Surabaya"])
employee_table.add_row(["ED20230604", "Olivia Smith", datetime.strptime("1998-02-14", "%Y-%m-%d").date(), datetime.strptime("2023-06-04", "%Y-%m-%d").date(), "Customer Service", "Customer Relations", "Intermediate", 6000000, "Part-Time", "Medan"])
employee_table.add_row(["ED20230705", "Isabella Martinez", datetime.strptime("1991-11-22", "%Y-%m-%d").date(), datetime.strptime("2023-07-05", "%Y-%m-%d").date(), "Finance", "Finance Manager", "Senior-level", 14000000, "Full-Time", "Yogyakarta"])
employee_table.add_row(["ED20230806", "Noah Garcia", datetime.strptime("1994-06-10", "%Y-%m-%d").date(), datetime.strptime("2023-08-06", "%Y-%m-%d").date(), "HR", "Recruiter", "Intermediate", 7000000, "Full-Time", "Jakarta"])
employee_table.add_row(["ED20230907", "Mia Davis", datetime.strptime("1995-12-20", "%Y-%m-%d").date(), datetime.strptime("2023-09-07", "%Y-%m-%d").date(), "Product Development", "Product Analyst", "Managerial-level", 15000000, "Full-Time", "Bandung"])
employee_table.add_row(["ED20231008", "James Wilson", datetime.strptime("1987-03-15", "%Y-%m-%d").date(), datetime.strptime("2023-10-08", "%Y-%m-%d").date(), "UX/UI Design", "UX Researcher", "Intermediate", 11000000, "Full-Time", "Surabaya"])
employee_table.add_row(["ED20231109", "Ava Brown", datetime.strptime("2002-08-30", "%Y-%m-%d").date(), datetime.strptime("2023-11-09", "%Y-%m-%d").date(), "Data Analysis", "Data Analyst", "Entry-level", 5000000, "Part-Time", "Medan"])
employee_table.add_row(["ED20231210", "Benjamin Taylor", datetime.strptime("1990-05-05", "%Y-%m-%d").date(), datetime.strptime("2023-12-10", "%Y-%m-%d").date(), "Logistics", "Logistics Manager", "Senior-level", 10000000, "Full-Time", "Yogyakarta"])

feedback_table = PrettyTable()

employee_id = "Employee_Id"
feedback_date = "Feedback_Date"
employee_name = "Employee_Name"
feedback = "Feedback"

feedback_table.field_names = [employee_id, feedback_date, employee_name, feedback]

feedback_table.align[feedback_date] = "r"
feedback_table.align[employee_name] = "l"
feedback_table.align[feedback] = "l"

feedback_table.add_row(["ED20190501", datetime.strptime("2024-05-12", "%Y-%m-%d").date(), "John Haryanto", "Tech Support needs access to paid tools to improve our performance."])
feedback_table.add_row(["ED20180302", datetime.strptime("2024-06-15", "%Y-%m-%d").date(), "Lisa Tanaka", "The marketing team requires more training on digital marketing strategies."])
feedback_table.add_row(["ED20200703", datetime.strptime("2024-07-20", "%Y-%m-%d").date(), "Ravi Kumar", "Product development needs more collaboration with the design team for better results."])
feedback_table.add_row(["ED20160204", datetime.strptime("2024-08-10", "%Y-%m-%d").date(), "Maria Andini", "As a data scientist, I suggest implementing better data collection processes."])
feedback_table.add_row(["ED20230105", datetime.strptime("2024-09-05", "%Y-%m-%d").date(), "Ethan Jones", "Customer support could improve with a more streamlined ticketing system."])
feedback_table.add_row(["ED20170606", datetime.strptime("2024-09-15", "%Y-%m-%d").date(), "Ayu Putri", "HR policies need to be more transparent to build trust within the company."])
feedback_table.add_row(["ED20220907", datetime.strptime("2023-10-12", "%Y-%m-%d").date(), "Samuel Robinson", "Sales training should focus more on customer relationship management techniques."])
feedback_table.add_row(["ED20151108", datetime.strptime("2023-11-08", "%Y-%m-%d").date(), "Tariq Basir", "Logistics requires more investment in software to enhance efficiency."])
feedback_table.add_row(["ED20240309", datetime.strptime("2023-11-25", "%Y-%m-%d").date(), "Nina Zhang", "The UX/UI team needs better feedback channels from users to iterate designs."])
feedback_table.add_row(["ED20141010", datetime.strptime("2023-12-01", "%Y-%m-%d").date(), "Daniella Herrera", "Finance needs a more robust forecasting tool to enhance budget accuracy."])

#Admin Functions
def admin():
    while True:
        print('\n[ADMIN PAGE]')
        print('1. Employee Database')
        print('2. Add Employee')
        print('3. Update Employee')
        print('4. Delete Employee')
        print('5. Exit')
        admin_input = int(input('Enter your option: '))

        if admin_input == 1:
            display_employee_database()
        elif admin_input == 2:
            add_employee()
        elif admin_input == 3:
            update_employee()
        elif admin_input == 4:
            delete_employee()
        elif admin_input == 5:
            print('Exiting admin page.')
            break
        else:
            print('Invalid option. Try again.')

def display_employee_database():
    while True:
        print('\n[EMPLOYEE DATABASE]')
        print('1. Display All Employee Data')
        print('2. Display All Employee Feedback on Company')
        print('3. Back to Admin Page')
        employee_database_input = int(input('Enter your option: '))

        if employee_database_input == 1:
            display_all_employee_data()
        elif employee_database_input == 2:
            display_employee_feedback()
        elif employee_database_input == 3:
            return
        else:
            print('Invalid input. Please try again.')

def display_all_employee_data():
    if len(employee_table.rows) == 0:
        print("\nData does not exist.")
    else:
        print("\nAll Employee Data:")
        print(employee_table)

        while True:
            print("\n[EMPLOYEE DATA OPTIONS]")
            print("1. Search Employee")
            print("2. Sort Employee Data")
            print("3. Back to Employee Database")
            data_option = int(input('Enter your option: '))

            if data_option == 1:
                search_column = input("Enter the column name to search (e.g., Employee_Id, Salary): ")
                search_value = input(f"Enter the value to search in {search_column}: ")

                if search_column in employee_table.field_names:
                    search_results = [row for row in employee_table.rows if str(row[employee_table.field_names.index(search_column)]).lower() == search_value.lower()]

                    if search_results:
                        print("\nSearch Results:")
                        for result in search_results:
                            print(result)
                    else:
                        print("No matching results found.")
                else:
                    print("Invalid column name. Please try again.")

            elif data_option == 2:
                sort_field = input("Enter the field to sort by (e.g., Employee_Id, Salary, Joining_Date): ")
                sort_order = input("Enter the sort order (ASC/DESC): ").upper()

                if sort_order == "ASC":
                    employee_table.sortby = sort_field
                    employee_table.reversesort = False
                elif sort_order == "DESC":
                    employee_table.sortby = sort_field
                    employee_table.reversesort = True
                else:
                    print("Invalid sort order. Please choose 'ASC' or 'DESC'.")

                print("\nSorted Employee Data:")
                print(employee_table)

            elif data_option == 3:
                return

            else:
                print("Invalid input. Please try again.")

def display_employee_feedback():
    if len(feedback_table.rows) == 0:
        print("\nData does not exist.")
    else:
        print("\nAll Employee Feedback Data:")
        print(feedback_table)

        while True:
            print("\n[FEEDBACK DATA OPTIONS]")
            print("1. Search Feedback by Column")
            print("2. Sort Feedback Data")
            print("3. Back to Employee Database")
            feedback_option = int(input('Enter your option: '))

            if feedback_option == 1:
                search_column = input("Enter the column name to search (e.g., Employee_Id, Feedback_Date): ")
                search_value = input(f"Enter the value to search in {search_column}: ")

                if search_column in feedback_table.field_names:
                    search_results = [row for row in feedback_table.rows if str(row[feedback_table.field_names.index(search_column)]).lower() == search_value.lower()]

                    if search_results:
                        print("\nSearch Results:")
                        for result in search_results:
                            print(result)
                    else:
                        print("No matching results found.")
                else:
                    print("Invalid column name. Please try again.")

            elif feedback_option == 2:
                sort_field = input("Enter the field to sort by (e.g., Employee_Id, Feedback_Date): ")
                sort_order = input("Enter the sort order (ASC/DESC): ").upper()

                if sort_order == "ASC":
                    feedback_table.sortby = sort_field
                    feedback_table.reversesort = False
                elif sort_order == "DESC":
                    feedback_table.sortby = sort_field
                    feedback_table.reversesort = True
                else:
                    print("Invalid sort order. Please choose 'ASC' or 'DESC'.")

                print("\nSorted Employee Feedback Data:")
                print(feedback_table)

            elif feedback_option == 3:
                return

            else:
                print("Invalid input. Please try again.")

def add_employee():
    while True:
        print('\n[ADD EMPLOYEE]')
        print('1. Create Employee Data')
        print('2. Back to Admin Page')
        add_input = int(input('Enter your option: '))

        if add_input == 1:
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            emp_birthdate = datetime.strptime(input("Enter Birthdate (YYYY-MM-DD): "), "%Y-%m-%d").date()
            emp_joining_date = datetime.strptime(input("Enter Joining Date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            emp_department = input("Enter Department: ")
            emp_job = input("Enter Job: ")
            emp_position = input("Enter Position: ")
            emp_salary = int(input("Enter Salary: "))
            emp_status = input("Enter Employment Status: ")
            emp_region = input("Enter Region: ")

            while True:
                add_confirmation = input("Are you sure you want to add this data? (yes/no): ")
                if add_confirmation.lower() == "yes":
                    employee_table.add_row([emp_id, emp_name, emp_birthdate, emp_joining_date, emp_department, emp_job, emp_position, emp_salary, emp_status, emp_region])
                    print("\nEmployee Data successfully saved.")
                    break
                elif add_confirmation.lower() == "no":
                    print("Data addition canceled.")
                    return
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.\n")
            break
        elif add_input == 2:
            return
        else:
            print("Invalid input. Please try again.")

def update_employee():
    while True:
        print('\n[UPDATE EMPLOYEE]')
        print('1. Update Employee Data')
        print('2. Back to Admin Page')
        update_input = int(input('Enter your option: '))

        if update_input == 1:
            emp_id = input("Enter Employee ID to update: ")
            for row in employee_table.rows:
                if row[0] == emp_id:
                    print(f"\nSelected Employee: {row}")

                    print("\nWhich column would you like to update?")
                    print("1. Employee Name")
                    print("2. Birthdate")
                    print("3. Joining Date")
                    print("4. Department")
                    print("5. Job")
                    print("6. Position")
                    print("7. Salary")
                    print("8. Employment Status")
                    print("9. Region")
                    column_choice = int(input("Enter the number of the column you want to update: "))

                    if column_choice == 1:
                        row[1] = input("Enter new Employee Name: ")
                    elif column_choice == 2:
                        row[2] = datetime.strptime(input("Enter new Birthdate (YYYY-MM-DD): "), "%Y-%m-%d").date()
                    elif column_choice == 3:
                        row[3] = datetime.strptime(input("Enter new Joining Date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                    elif column_choice == 4:
                        row[4] = input("Enter new Department: ")
                    elif column_choice == 5:
                        row[5] = input("Enter new Job: ")
                    elif column_choice == 6:
                        row[6] = input("Enter new Position: ")
                    elif column_choice == 7:
                        row[7] = int(input("Enter new Salary: "))
                    elif column_choice == 8:
                        row[8] = input("Enter new Employment Status: ")
                    elif column_choice == 9:
                        row[9] = input("Enter new Region: ")
                    else:
                        print("Invalid column choice. Please try again.")
                        continue

                    print(f"\nEmployee {emp_id} data successfully updated.")
                    print(f"{row}\n")

                    break
            else:
                print("Employee data does not exist.")
        elif update_input == 2:
            return
        else:
            print("Invalid input. Please try again.")

def delete_employee():
    #4. Delete Employee
    while True:
        print('\n[DELETE EMPLOYEE]')
        print('1. Delete Employee Data')
        print('2. Back to Admin Page')
        delete_input = int(input('Enter your option: '))

        if delete_input == 1:
            emp_id = input("Enter Employee ID to delete: ")
            for row in employee_table.rows:
                if row[0] == emp_id:

                    #confirmation to delete the data
                    while True:
                        delete_confirmation = input("Are you sure you want to delete this data? (yes/no): ")
                        if delete_confirmation.lower() == "yes":
                            employee_table.del_row(employee_table.rows.index(row))
                            print(f"\nEmployee {emp_id} successfully deleted.")
                            print(f"{row}\n")
                            break
                        elif delete_confirmation.lower() == "no":
                            print("Deletion canceled.")
                            break
                        else:
                            print("\nInvalid input. Please enter 'yes' or 'no'.\n")
            else:
                print("Employee data does not exist.")
        elif delete_input == 2:
            return  # Go back to the admin page
        else:
            print("Invalid input. Please try again.")

#User Function
user_credentials = {'user': 'myuser'}

def user():
  while True:
    print('\n[USER PAGE]')
    print('1. Employee Feedback Form')
    print('2. Exit')

    user_input = int(input('Enter a number to select your option:'))

    if user_input == 1:
            add_feedback()
    elif user_input == 2:
        print('Exiting admin page.')
        break
    else:
        print('Invalid option. Try again.')

def add_feedback():
    while True:
        add_employee_id = input('\nEnter your employee id: ')
        selected_employee_id = print(f"'{add_employee_id}'")

        selected_row = employee_table.rows[employee_id == selected_employee_id]

        if selected_row:
            selected_employee_name = selected_row[1]
            print(f"\nEmployee_id: {add_employee_id}\nSelected Employee: {selected_employee_name}")

            feedback_date = datetime.now().strftime("%Y-%m-%d")
            feedback = input("Enter Feedback: ")

            #input feedback confirmation
            while True:
                feedback_confirmation = input("Are you sure you want to submit this feedback? (yes/no): ")
                if feedback_confirmation.lower() == "yes":
                    feedback_table.add_row([add_employee_id, feedback_date, selected_employee_name, feedback])
                    print("\nThank you for filling the feedback form.")

                    filtered_feedback = PrettyTable()
                    filtered_feedback = feedback_table
                    print(filtered_feedback)

                    return
                elif feedback_confirmation.lower() == "no":
                    print("Feedback submission canceled.")
                    return
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.\n")
        else:
            print("Employee ID not found. Please try again.")

#Login Function
def login():
    #Login Page
    while True:
        print('\n[LOGIN PAGE]')
        print('1. Admin\n2. User')
        role = int(input('Enter a number to select your role: '))

        if role == 1:
            attempt_count = 0
            max_attempts = 3
            while attempt_count < max_attempts:
                username = input('Enter admin username: ')
                password = input('Enter admin password: ')
                if username in admin_credentials and admin_credentials[username] == password:
                    admin()  # Admin menu
                    break
                else:
                    attempt_count += 1
                    print(f'Invalid username or password. Attempt {attempt_count}/{max_attempts}\n')
                    if attempt_count == max_attempts:
                        print('Too many failed attempts. Exiting....')
                        return  # Exit after too many failed attempts
        elif role == 2:
            attempt_count = 0
            max_attempts = 3
            while attempt_count < max_attempts:
                username = input('Enter user username: ')
                password = input('Enter user password: ')
                if username in user_credentials and user_credentials[username] == password:
                    user()  # Admin menu
                    break
                else:
                    attempt_count += 1
                    print(f'Invalid username or password. Attempt {attempt_count}/{max_attempts}\n')
                    if attempt_count == max_attempts:
                        print('Too many failed attempts. Exiting....')
                        return  # Exit after too many failed attempts
        else:
            print('Invalid role. Please enter 1 for Admin or 2 for User.\n')

login()