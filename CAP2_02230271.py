# Sangay Tenzin
# BE Mechanical
# 02230271

# References:
# https://youtu.be/julcNz6rWVc?si=_gXjaxS7MZYf_1tr
# https://youtu.be/ztDK6u-XR6E?si=K-jq6vzVn4VrPkgg
# https://youtu.be/BRssQPHZMrc?si=awzavYv49OCtvdKM

import os # This line imports the os module for operating system related functionalities
import random # This line imports the random module for generating random values
import string # This line Imports the string module for string manipulation operations

# Defining the base class for Accounts
class Account:
    def __init__(self, acc_number, password, acc_type, bal=0):  # Constructing line to initialize Account objects
        self.account_number = acc_number  # Assigning account number 
        self.password = password # Assigning password 
        self.account_type = acc_type # Assigning account type 
        self.balance = bal # Assigning balance, defaulting to 0 if no initial deposit provided

# Function to deposit money into the user's account
    def deposit(self, amount):  
        if amount > 0: # Checking if the amount is positive and greater than 0
            self.balance += amount  # Adding the deposited amount to the balance
            print(f"Your account has been deposited with Nu.{amount}. Your new balance is Nu.{self.balance}") # Printing the deposit confirmation and new balance
        else:
            print("Invalid amount! Please try again with valid amount.")  # Printing error message for invalid amount and deposition

# Function to withdraw money from the user's account
    def withdraw(self, amount):  
        if amount > 0 and amount <= self.balance: # Checking if the withdrawal amount is positive and within the balance of the user's account
            self.balance -= amount # Subtracting the amount to the balance
            print(f"You account has been withdrawn with Nu.{amount}. Your new balance is Nu.{self.balance}")  # Printing withdrawal confirmation and new balance
        else:
            print("Insufficient money in your account.") # Printing error message for invalid amount and withdrawal

# Function to save account information to a file
    def save_to_file(self, file_name='accounts.txt'):
        with open(file_name, 'a') as f:  # Opening the file in append mode
            f.write(f"{self.account_number},{self.password},{self.account_type},{self.balance}\n")  # Writing account information to the file


# Defining the PersonalAccount class inheriting from Account
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0): # Constructing to initialize PersonalAccount objects
        super().__init__(account_number, password, 'Personal', balance) # Calling the superclass constructor with the account type as 'Personal'

# Defining the BusinessAccount class inheriting from Account
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0): # Constructing to initialize BusinessAccount objects
        super().__init__(account_number, password, 'Business', balance) # Calling the superclass constructor with the account type as 'Business'

# Function to generate a random account number
def generate_account_number():
    return ''.join(random.choices(string.digits, k=9)) # Generating a random 9-digit account number for the user using digits

# Function to generate a random password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))  # Generating a random 6-character password for the user using letters and digits

# Function to load account information from file
def load_accounts(file_name='accounts.txt'):
    accounts = {} # This is the dictionary to store loaded accounts
    if os.path.exists(file_name): # Checking if the file exists
        with open(file_name, 'r') as f: # Opening the file in read mode
            lines = f.readlines() # Reading all lines from the file
            for line in lines:  # Iterating over each line
                account_number, password, account_type, balance = line.strip().split(',')  # This line extracts account information from the line
                balance = float(balance) # Converting balance to float digits
                print(f"Registered account: {account_number}, {password}, {account_type}, {balance}")   
                if account_type == 'personal': # Checking if the account type is personal
                    account = PersonalAccount(account_number, password, balance) # If personal then creating a PersonalAccount object
                elif account_type == 'business': # Checking if the account type is business
                    account = BusinessAccount(account_number, password, balance) # If business creating a BusinessAccount object
                accounts[account_number] = account  # This line adds the account to the dictionary
    return accounts  # Returning the loaded accounts dictionary


#Function to login to an account
def login(accounts):
    account_number = input("Enter your account number: ") # Prompting the user to enter their account number
    password = input("Enter your password: ") # Prompting the user to enter their password
    
    account = accounts.get(account_number) # Getting the account object corresponding to the account number
    if account and account.password == password: # Checking if the user account exists and their password is correct
        print("You have successfully logged in.")  # Printing login success message if the account number and password was correct
        return account  # Returning the logged-in account object
    else:
        print("Invalid account number or password. Please try again.")  # Printing login failure message
        return None # Returning None if login fails


#Function to transfer the fund
def fund_transfer(accounts, from_account):
    to_account_number = input("Enter the recipient's account number: ") # Prompting the user to enter recipient's account number
    amount = float(input("Enter the amount to send: "))  # Prompting the user to enter the amount of money to send
    if to_account_number in accounts:   # Checking if the recipient's account exists
        if from_account.balance >= amount:  # Checking if the sender's account has sufficient ammount in their balance
            from_account.withdraw(amount) # Withdrawing the amount from the sender's account
            accounts[to_account_number].deposit(amount) # Depositing the amount to the recipient's account
            print(f"You have successfully transferred Nu.{amount} to {to_account_number}.") # Printing fund transfer confirmation and new balance in the sender's and recipient's account
        else:
            print("Insufficient money in your account.")  # Printing error message for insufficient balance in the account
    else:
        print("Recipient account not found. Please try agian with a valid account number")  # Printing error message if recipient's account is not found


def main():  # Implementation details omitted for brevity
    accounts = load_accounts() # Loading accounts from file

    while True:
        print("\n Welcome! We offer the following services:") # Printing main menu for the users with the foloowing options to choose
        print("1. Create a new account.")
        print("2. Login to your existing account.")
        print("3. Exit")
        choice = input("Enter your choice: ")  # Prompting the user to enter their choice

# Handling choice 1: Create a new account
        if choice == '1':   
            account_type = input("Select Account Type (Personal/Business):")  # Prompting the user to select the account type to use
            initial_deposit = float(input("Enter initial deposit: "))  # Prompting the user to enter initial deposit amount in their account
            if account_type in ['Personal', 'Business']:  # Checking if the selected account type is valid i.e, Personal/Business
                account_number = generate_account_number()  # Generating a random account number for the user
                password = generate_password()  # Generating a random password for the user
                if account_type == 'Personal':  # Checking if the account type is personal
                    account = PersonalAccount(account_number, password, initial_deposit)  # If personal then creating a PersonalAccount object
                else:
                    account = BusinessAccount(account_number, password, initial_deposit) # Creating a BusinessAccount object if the account type is business
                account.save_to_file() 
                accounts[account_number] = account
                print(f"Your account has been created successfully!")
                print(f"Your new account number is {account_number} and password is {password}")
                print(f"Please do not forget your account number and password!")
            else:
                print("Invalid account type selected. Please select a valid detail.")

 #Handling choice 2: Login to your existing account
        elif choice == '2': 
            account = login(accounts) # Attempting to log in using the provided accounts
            if account:  # Checking if login was successful
                # Starting account menu loop
                while True:  
                    print("\nAccount Menu:")
                    print("1. Check your balance.")
                    print("2. Deposit money to your account. ")
                    print("3. Withdraw money from your account. ")
                    print("4. Transfer funds.")
                    print("5. Delete your account.")
                    print("6. Logout.")
                    account_choice = input("Enter your choice of service: ")  # Prompting the user to select a service

                    # Handling balance checking in account menu 
                    if account_choice == '1':  
                        print(f"Your Balance: Nu.{account.balance}")   # Printing the account balance

                    # Handling depositing money in account menu
                    elif account_choice == '2': 
                        amount = float(input("Enter amount to deposit: "))  # Prompting the user to enter deposit amount
                        account.deposit(amount) # Depositing the specified amount to the account

                    # Handling withdrawing money in accounr menu
                    elif account_choice == '3':  
                        amount = float(input("Enter amount to withdraw: "))  # Prompting the user to enter withdrawal amount
                        account.withdraw(amount) # Withdrawing the specified amount from the account

                    # Handling fund transfer in account menu
                    elif account_choice == '4':  
                        fund_transfer(accounts, account)  # Initiating fund transfer process

                     # Handling account deletion in account menu
                    elif account_choice == '5': 
                        del accounts[account.account_number]   # Deleting the account from the dictionary of accounts

                        print("Your account has been deleted successfully.") # Printing deleting success message
                        break

                     # Handling logout in account menu
                    elif account_choice == '6':  
                        print("Logged out successfully.") # Printing logout success message
                        break  # Exiting the account menu loop
                    else:  # Handling invalid choice
                        print("Invalid choice. Please try again.")  # Printing error message for invalid choice

# Handling choice 3: Exit   
        elif choice == '3':
            print("Thank you for availing our servive. Do visit again!") # Printing exit message
            break  # Exiting the main loop
        else:
            print("Invalid choice. Please try again.") # Printing error message for invalid choice

# Calling the main function
if __name__ == "__main__":
    main()  