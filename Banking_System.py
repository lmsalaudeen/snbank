# Create staff.txt
# Create customer.txt

import random
import datetime
import os


# login and check if login details correct
def check_login_details():
    with open("staff.txt") as staff_file:
        text = staff_file.read().strip()
        while True:
            try:
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                if username == "" and password == "":
                    continue
                if username and password in text:
                    print("Login Successful")
                    # create file to store login session
                    time = datetime.datetime.now()
                    session_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    with open("session.txt", "a") as user_session:
                        user_session.write("\n" + username + " " + password + " " + session_time)
                    break
                else:
                    raise Exception("Username or password incorrect. Try again")
            except Exception as incorrect:
                print(incorrect)


# input account number to fetch account details
def input_account_number():
    with open("customer.txt") as customer_file:
        text = customer_file.read().strip().split()
        while True:
            try:
                account_number_request = input('Please enter your account number: ')
                if account_number_request == "":
                    continue
                if account_number_request in text:
                    print(f"Your account details are: {text}")
                    break
                else:
                    raise Exception("Incorrect account number! Try again")
            except Exception as incorrect:
                print(incorrect)


# generate 10 digit account number
def gen_account_number():
    account_number = int(''.join(str(random.randint(0, 9)) for i in range(10)))
    return account_number


# input account details for account creation
def input_account_details():
    account_name = input('Please enter account name: ')
    opening_balance = input('Please enter opening balance: ')
    account_type = input('Please enter account type: ')
    account_email = input('Please enter account email: ')
    gen_account_number()
    account_details = [account_name, opening_balance, account_type, account_email, gen_account_number()]
    with open("customer.txt", "a") as customer_file:
        customer_file.write(
            f"\nAccount_Name:{account_name} Opening_Balance:{opening_balance} Account_Type:{account_type} "
            f"Account_Email:{account_email} Account_Number:{str(gen_account_number())}")
    return account_details


start = True
while start:
    try:
        run = int(input('''
    Press 1 for Staff Login
    Press 2 to Close App
            '''))
        if run == 1:
            check_login_details()
            # Staff Login
            staff_login = True
            while staff_login:
                # Logged in
                try:
                    login_options = int(input('''
                        Enter 1 to Create new bank account

                        Enter 2 to Check Account Details

                        Enter 3 to Logout
                        '''))

                    # 1: Create Account
                    if login_options == 1:
                        new_bank_account = True
                        while new_bank_account:
                            input_account_details()
                            # show customer account number
                            print(f"Account created! Your account number is: {gen_account_number()}")
                            # bring back login options
                            new_bank_account = False
                            staff_login = True

                    # 2: Check account details
                    elif login_options == 2:
                        check_account_details = True
                        while check_account_details:
                            input_account_number()
                            check_account_details = False
                            staff_login = True

                    # Log out
                    elif login_options == 3:
                        logout = True
                        while logout:
                            if os.path.exists("session.txt"):
                                os.remove("session.txt")
                            start = True
                            staff_login = False
                            logout = False
                    else:
                        print('Enter 1, 2 or 3')


                except ValueError:
                    print("Invalid input!")
                    staff_login = True

        # Close App
        elif run == 2:
            start = False


        # Number other than 1 or 2
        elif run != 1 or run != 2:
            print('Invalid input. Please enter 1 for staff login or 2 to close app')

    except ValueError:
        print('Invalid input! Enter a number')

