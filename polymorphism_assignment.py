

#Parent class
class Management:
    name = ""
    email = ""
    password = ""

    def login_info(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child class
class Employee(Management):
    department = ""
    wage = ""
    employee_number = ""

    def login_info(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_employee_number = input("Enter your employee number: ")
        if (entry_email == self.email and entry_employee_number == self.employee_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The employee number or email is incorrect.")

#Child class
class Customer(Management):
    address = ""
    phone_number = ""
    orders = ""
    passcode = ""

    def login_info(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_passcode = input("Enter your password: ")
        if (entry_email == self.email and entry_passcode == self.passcode):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The passcode or email is incorrect.")


#Invokes the methods inside each class
manager = Management()
manager.login_info()

employees = Employee()
employees.login_info()

user = Customers()
user.login_info()
