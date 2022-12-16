# Create dict to hold employee information
employee_data = {
    "E00123": {
        "name": "Aadya Khan",
        "salary": {
            "current": 38566,
            "history": {}
        },
        "leave": {
            "current": 25,
            "history": {}
        }
    },
    "E01033": {
        "name": "John Smith",
        "salary": {
            "current": 29400,
            "history": {
                2018: {
                    "basic": 29400,
                    "overtime": 2587
                }
            }
        },
        "leave": {
            "current": 25,
            "history": {
                2016: 22
            }
        }
    }
}

def get_employee(employee_data, employee_id):
    return employee_data[employee_id]


def get_name(employee):
    return employee["name"]


def get_salary(employee):
    return employee["salary"]


def get_annual_leave(employee):
    return employee["annual_leave"]