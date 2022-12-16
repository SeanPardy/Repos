"""
Name: Sean Pardy
ID: R00186157
"""
import socket
from employees_info import employee_data

header = 64
port = 5050
server_format = 'utf-8'
disconnect = "!dc"
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)


def send(msg):
    message = msg.encode(server_format)
    msg_len = len(message)
    send_len = str(msg_len).encode(server_format)

    send_len += b' ' * (header - len(send_len))
    client.send(send_len)
    client.send(message)


print("HR System 1.0")
# Loop until the user wants to exit
while True:
    # Ask the user for an employee id
    employee_id = input("What is the employee id? ")
    send(employee_id)

    # Check if the employee id is valid
    if employee_id not in employee_data:
        print("Sorry... I don’t recognize that employee id")
        continue

    # Ask the user what type of query they want to make
    while True:
        query_type = input("Salary (S) or Annual Leave (L) Query? ")
        send(query_type)

        # Check if the query type is valid
        if query_type not in ["S", "L", "s", "l"]:
            print("Invalid query type")
        break

    # If the query is for salary information
    if query_type in ["S", "L", "s", "l"]:
        # Ask the user if they want current or total salary information
        salary_type = input("Current salary (C) or total salary (T) for year? ")
        send(salary_type)

        # Check if the salary type is valid
        if salary_type not in ["C", "T", "c", "t"]:
            print("Invalid salary type")
            continue

        # If the user wants current salary information
        if salary_type in ["C", "c"]:
            # Print the current salary for the employee
            print(
                f"{employee_data[employee_id]['name']}: Current basic salary: {employee_data[employee_id]['salary']['current']}")

        # If the user wants total salary information for a specific year
        elif salary_type in ["T", "t"]:
            # Ask the user for a year
            year = input("What year? ")
            send(year)

            # Check if the year is valid
            if year not in employee_data[employee_id]['salary']['history']:
                print("Sorry... I don’t have salary information for that year")
                continue

            # Print the total salary for the employee in the specified year
            salary_info = employee_data[employee_id]['salary']['history'][year]
            print(
                f"{employee_data[employee_id]['name']}: Total Salary for {year}: Basic pay, {salary_info['basic']}; Overtime, {salary_info['overtime']}")

    # If the query is for leave information
    elif query_type in ["L", "l"]:
        # Ask the user if they want current or leave taken information for a specific year
        leave_type = input("Current Entitlement (C) or Leave taken for year (Y)? ")
        send(leave_type)

        # Check if the leave type is valid
        if leave_type not in ["C", "Y", "c", "y"]:
            print("Invalid leave type")
            continue
        elif leave_type == "!dc":
            print("Goodbye")
            break

        # If the user wants current leave entitlement information
        if leave_type in ["C", "c"]:
            # Print the current leave entitlement for the employee
            print(
                f"{employee_data[employee_id]['name']}: Current annual leave entitlement: {employee_data[employee_id]['leave']['current']} days")

        # If the user wants leave taken information for a specific year
        elif leave_type in ["Y", "y"]:
            # Ask the user for a year
            year = input("What year? ")
            send(year)

            # Check if the year is valid
            if year not in employee_data[employee_id]['leave']['history']:
                print("Sorry... I don’t have leave information for that year")
                continue

            # Print the leave taken for the employee in the specified year
            leave_taken = employee_data[employee_id]['leave']['history'][year]
            print(f"{employee_data[employee_id]['name']}: Leave taken in {year}: {leave_taken} days")

        # Ask the user if they want to continue or exit
    continue_or_exit = input("Would you like to continue (C) or exit (X)? (Please use capitals only) ")
    send(continue_or_exit)
    # Check if the user wants to exit
    if continue_or_exit == "X":
        print("Goodbye")
        break

send(disconnect)
