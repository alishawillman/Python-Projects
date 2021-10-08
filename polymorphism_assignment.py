

#Parent class
class Management:
    name = "Jamie"
    email = "jamie@gmail.com"
    password = "password123"

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
    department = "store"
    wage = "15.00"
    employee_number = "1234"

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
    address = "100 B St"
    phone_number = "111-111-1111"
    orders = "12"
    passcode = "2345"

    def login_info(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_passcode = input("Enter your passcode: ")
        if (entry_email == self.email and entry_passcode == self.passcode):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The passcode or email is incorrect.")


#Invokes the methods inside each class
manager = Management()
manager.login_info()

employees = Employee()
employees.login_info()

user = Customer()
user.login_info()
