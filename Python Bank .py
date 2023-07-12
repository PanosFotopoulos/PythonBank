#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import datetime
import uuid
import getpass


class Account():
    def __init__(self):
        self.withdrawls_times = 0
        self.days_count = 0
        self.default_value = 0
        self.customer_id = 0
        self.name = 1
        self.tax_id = 0
        self.total_account_balance = 0
        self.ck_account = CheckingAccount
        self.sv_account = SavingsAccount
        self.account_type = ''
        self.action = ''
        self.amount = 0
        self.account_type_num = ''

    def initialize_sublcass_instances(self,customer_id,account_type,action,default_value,days_count,withdrawls_times):
        self.ck_account = CheckingAccount(customer_id,account_type,action,default_value)
        self.sv_account = SavingsAccount(customer_id,account_type,action,default_value,days_count,withdrawls_times)
    
    def ask_user_for_action(self):
        while self.action.lower() not in ['login','register','withdraw','deposit','return','quit']:
            self.action = input('Please choose from login register or quit!')
        if self.action.lower() == "login":
            self.login()
        elif self.action.lower() == "register":
            self.register()
        elif self.action.lower() == "withdraw":
            self.withdraw()
        elif self.action.lower() == "deposit":
            self.deposit()
        elif self.action.lower() == 'return':
            self.returning()
        elif self.action.lower() == 'quit':
            self.quit()
     
    def register(self): 
        while True:
            self.name = input("Provide a username or type 'back' in order to login or register!: ") 
            if self.name.lower() == 'back':
                self.ask_user_for_action()
                break
            elif not self.name.isalpha():
                print("Username can only contain alphabetic characters!")
            else:
                break
        while self.tax_id <= 0:
            try:
                self.tax_id = int(input("Hello, please input a Tax ID: "))
                if self.tax_id <= 0:
                    print("Your Tax ID must be positive")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            else:
                self.customer_id = str(uuid.uuid4())
                account_details = {
                    'name' : self.name.title(),
                   'tax_id' : self.tax_id,
                    'Total Balance': 0,
                   'accounts': {
                        'Checking Account': self.default_value,
                        'Savings Account': self.default_value,
                        'Business Account': self.default_value
                    }
                }
                database[self.customer_id] = account_details
            self.initialize_sublcass_instances(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times)
            self.count_day()
            print(f'Welcome Mr/Mrs {self.name.title()}')
            print(f'Your unique ID is {self.customer_id} \nThis is also your password you can log in with to your bank account like your credit card!')
            print("Let's get started! For now, we create three different accounts for you:")
            print("Checking Account serve as versatile tools that allow individuals store funds and easily make transactions  ")
            print("Savings Accounts offer individuals a secure means to accumulate funds and earn interest")
            self.show_account_info(True)      
            self.choosingaccount()
                  
    def login(self):    
        while True:
            user_id = getpass.getpass('Hello, Please enter your user ID.\nIf you want to Register type Register.\nIf you want to Exit type Exit\n ID:  ')
            if user_id in database.keys() or user_id =='Register' or user_id == 'Exit':
                self.customer_id = user_id
                print(f"Welcome Mr/Mrs {database[self.customer_id]['name']}, we are happy to see you again!")
                self.show_account_info(False)
                self.ask_user_for_account_action() 
    def quit(self):
        print("Thank you for using Python Bank. Have a nice day!")
        self.action = ''
        sys.exit()
        
    def choosingaccount(self):
        self.account_type_num = ''
        while self.account_type_num not in ['1','2','3']:
            print('1. Checking Account')
            print('2. Savings Account')
            print('3. Business Account')
            self.account_type_num = (input('Please choose between a number to get in corresponding account! '))
            self.ask_user_for_account_action()
  
    def show_account_info(self,register):
        print ('Account Details')
        if register :
            print (f'User ID: {self.customer_id} ----- You will need this to login!')
        else:
            print(f"Name : {database[self.customer_id]['name']}")
            print(f"Tax ID: {database[self.customer_id]['tax_id']}")
            print(f"Checking's Account Balance is : {database[self.customer_id]['Checking Account']}" +'€')
            print(f"Saving's Account Balance is : {database[self.customer_id]['Savings Account']}"+'€')

    def ask_user_for_account_action(self):
        if self.account_type_num == "1":
            self.account_type = ('Checking Account')
            print('Checking Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw? ' )
            if self.action.lower() == "deposit":
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).deposit()
            elif self.action.lower() == 'withdraw':
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).withdraw()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw':
                print('Please enter a valid action!')
            self.ck_account.ask_user_for_action()
            
            
            
        elif self.account_type_num == "2":
            self.account_type = ('Savings Account')
            print('Savings Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw? ' )
            if self.action.lower() == "deposit":
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).deposit()
            elif self.action.lower() == 'withdraw':
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).withdraw()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw':
                print('Please enter a valid action!')
            self.sv_account.ask_user_for_action()
            
                  
    def deposit(self):
        self.get_amount_input()
        old_subclass_account_balance = 0
        print('Deposit Accepted')
        print(f'edw eina it {self.account_type} + {self.name}')
        old_subclass_account_balance = database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        new_subclass_account_balance = old_subclass_account_balance + self.amount
        database[self.customer_id]['accounts'][self.account_type] = new_subclass_account_balance
        print(f'Your Current Balance on {self.account_type} is ' + "%.2f" % new_subclass_account_balance + '€')
        self.update_total_balance()

    def withdraw(self):
        self.get_amount_input()
        account_balance = database[self.customer_id]['accounts'].get(self.account_type, 0)
        if self.amount <= account_balance:
            new_balance = account_balance - self.amount
            database[self.customer_id]['accounts'][self.account_type] = new_balance
            print('Withdraw Accepted')
            print('Your total balance is ' + "%.2f" % database[self.customer_id]['Total Balance'] + '€')
            print(f'Your {self.account_type} balance is ' + "%.2f" % new_balance + '€')
        else:
            print('Insufficient funds. Unable to withdraw.')

            
            
    def get_amount_input(self):
            while True:
                self.amount = int(input("Please enter a valid amount: "))
                if type(self.amount)!= int:
                    print("Amount cannot be alphanumeric.")
                elif self.amount <= 0:
                    print("Amount needs to be a positive integer.")
                else:
                    break
                    
    def returning(self):
        decision = ''
        while decision.lower() != 'yes' and decision.lower() != 'no':
               decision = input("Do you want to do another transaction? Yes/No:\n Press 'back' if you want to change account")
        else:
            if decision.lower() == 'yes':
                self.account_type = ''
                self.account_type_num = 0
                self.choosingaccount()
            elif decision.lower() == 'no':
                self.quit()
                
    def update_total_balance(self):
        total_balance = 0
        for account_type, balance in database[self.customer_id]['accounts'].items():
            total_balance += balance
        database[self.customer_id]['Total Balance'] = total_balance
        
    def count_day(self):
        self.current_date = datetime.date.today()
        self.days_count += 1
        if self.days_count == 30:
            self.days_count = 0
           
        
class CheckingAccount(Account):
    def __init__(self, customer_id, account_type, action, default_value):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance = database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        
        
    def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()

    def withdraw(self):
        super().withdraw()
        super().update_total_balance()
        self.action = ''
        super().returning()

class SavingsAccount(Account):
    def __init__(self, customer_id, account_type, action, default_value,days_count,withdrawls_times):
        super().__init__()
        self.days_count = days_count
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance = database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        self.withdrawls_times = withdrawls_times
        
    def count_withdrawls(self):
        self.withdrawls_times += 1  
        print (f' eimai sto count {self.withdrawls_times}')
        if self.withdrawls_times > 3 and self.days_count < 30:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            
    
    def calculate_the_presentage_of_last_day(self):
        value = database[self.customer_id]['accounts'][account_type]
        last_day_value =value + value*1/100
        last_day_value = database[self.customer_id]['accounts'][account_type]


    def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()
  

    def withdraw(self):
        self.count_withdrawls()
        if self.withdrawls_times > 3 and self.days_count < 30:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            return
        super().withdraw()
        super().update_total_balance()
        self.action = ""
        super().returning()

