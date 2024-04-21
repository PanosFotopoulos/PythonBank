#!/usr/bin/env python
# coding: utf-8

# In[1]:

============================================================DATABABSE & JSON CONVERTER(LOGIN SECTION)==========================================================
database = {}   

import csv
import ast

def csv_to_dict(csv_file):
    data_dict = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts = ast.literal_eval(row['accounts'])
            data_dict[row['uuid']] = {
                'name': row['name'],
                'tax_id': int(row['tax_id']),
                'Total Balance': int(row['Total Balance']),
                'accounts': accounts
            }
    return data_dict


database = csv_to_dict("OfficialDB.csv")      
database




=======================================================================FINAL PROJECT============================================================================
==========================================================================4/21==================================================================================
import sys
import datetime
import uuid
import getpass
from datetime import datetime
import pandas as pd
import csv
import os


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
        self.dg_account= DepositGuardAccount
        self.bs_account = BusinessAccount
        self.account_type = ''
        self.action = ''
        self.amount = 0
        self.account_type_num = ''

        
        
    def initialize_sublcass_instances(self,customer_id,account_type,action,default_value,days_count,withdrawls_times):
        self.ck_account = CheckingAccount(customer_id,account_type,action,default_value)
        self.sv_account = SavingsAccount(customer_id,account_type,action,default_value,days_count,withdrawls_times)
        self.dg_account = DepositGuardAccount(customer_id,account_type,action,default_value)
        self.bs_account = BusinessAccount(customer_id,account_type,action,default_value,days_count)
   


    def ask_user_for_action(self):
        while self.action.lower() not in ['login','register','withdraw','deposit','return','quit','yes','no']:
            self.action = input('Welcome to Python Bank!\nWould you like to login or register?')
        if self.action.lower() == "login":
            self.login()
        elif self.action.lower() == "register":
            self.register()
        elif self.action.lower() == ["withdraw"]:
            self.withdraw()
        elif self.action.lower() == ["deposit",'yes']:
            self.deposit()
        elif self.action.lower() == ['return','no']:
            self.returning()
        elif self.action.lower() == 'quit':
            self.quit()
     
    
    
    def register(self): 
        while True:
            self.name = input("Provide a username or type 'back' in order to login!: ") 
            if self.name.lower() == 'back':
                self.back()
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
                        ' DepositGuard Account': self.default_value,
                        'Business Account': self.default_value
                    }
                }
            database[self.customer_id] = account_details
            self.initialize_sublcass_instances(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times)
            print(f'Welcome Mr/Mrs {self.name.title()}')
            print(f'Your unique ID is {self.customer_id} \nThis is also your password you can log in with to your bank account like your credit card!')
            print("Let's get started! For now, we create three different accounts for you:")
            print("Checking Account serve as versatile tools that allow individuals store funds and easily make transactions  ")
            print("Savings Accounts offer individuals a secure means to accumulate funds and earn interest")
            print('DepositGuard Account allows withdrawals in person at the bank, ensuring maximum security for your funds."')
            print("Business accounts accrue a 12% balance increase on the first day of every month.")
            self.show_account_info(True)      
            self.choosingaccount()
      
    
    
    def login(self):
        while True:
            self.user_id = str(getpass.getpass('Hello, Please enter your user ID.\nIf you want to Register type Register.\nIf you want to Exit type Exit\n ID:  '))
            if self.user_id in database:
                self.customer_id = self.user_id
                self.initialize_sublcass_instances(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times)
                print(f"Welcome Mr/Mrs {database[self.customer_id]['name']}, we are happy to see you again!")
                self.show_account_info(False)
                self.choosingaccount()
                break
    
        
        
    def quit(self):
        print("Thank you for using Python Bank. Have a nice day!")
        fieldnames = ['uuid','name','tax_id','Total Balance','accounts']
        with open('OfficialDB.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for random_number, inner_dict in database.items():
                row = {'uuid': random_number}
                row.update(inner_dict)
                writer.writerow(row)
                self.action = ''
        sys.exit
    
    
    
    def csv_to_nested_dict1(self,csv_file):
        database = {}
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_id = uuid.UUID(row['uuid'])
                name = row['name']
                tax_id = int(row['tax_id'])
                total_balance = int(row['Total Balance'])
                accounts = eval(row['accounts']) 
     
    
    
    def choosingaccount(self):
        self.account_type_num = ''
        while self.account_type_num not in ['1','2','3','4']:
            print('--|---------------------|')
            print('1.|   Checking Account  |')
            print('--|---------------------|')
            print('2.|   Savings Account   |')
            print('--|---------------------|')
            print('3.| DepositGuard Account|')
            print('--|---------------------|')
            print('4.|   Business Account  |')
            print('--|---------------------|')
            self.account_type_num = (input('Please choose between a number to get in corresponding account! '))
            self.ask_user_for_account_action()
  


    def show_account_info(self,register):
        print ('Account Details')
        if register :
            print (f'User ID: {self.customer_id} ----- You will need this to login!')
        else:
            print(self.customer_id)
            print(f"Name : {database[self.customer_id]['name']}")
            print(f"Tax ID: {database[self.customer_id]['tax_id']}")
            print(f"Your Total Account Balance is : {database[self.customer_id]['Total Balance']}"+'€')
            print(f"• Checking's Account Balance is : {database[self.customer_id]['accounts']['Checking Account']}" +'€')
            print(f"• Saving's Account Balance is : {database[self.customer_id]['accounts']['Savings Account']}"+'€')
            print(f"• DepositGuard's Account Balance is : {database[self.customer_id]['accounts']['Checking Account']}" +'€')
            print(f"• Business's Account Balance is : {database[self.customer_id]['accounts']['Business Account']}"+'€')

          
        
    def ask_user_for_account_action(self):
        if self.account_type_num == "1":
            self.account_type = ('Checking Account')
            print('You are Currently in your Checking Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).deposit()
            elif self.action.lower() == 'withdraw':
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() == 'quit':
                self.quit()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
        elif self.account_type_num == "2":
            self.account_type = ('Savings Account')
            print('Savings Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).deposit()
            elif self.action.lower() == 'withdraw':
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
        elif self.account_type_num == '3':
            self.account_type = ('DepositGuard Account')
            print('DepositGuard Account')
            self.action = ''
            self.action = input('DepositGuard Account only allows deposits, not withdrawals.\nDo you want to continue? Yes/No')
            if self.action.lower() == 'yes':
                DepositGuardAccount(self.customer_id,self.account_type,self.action,self.default_value).deposit()
            elif self.action == 'no':
                self.back()
            else:
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
        elif self.account_type_num == '4':
            self.account_type = ('Business Account')
            print('Business Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                BusinessAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count).deposit()
            elif self.action.lower() == 'withdraw':
                BusinessAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() == 'quit':
                self.quit()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
        else:
            print('Please choose a valid account!')
     
    
    
    def back(self,go_back=True):
        if self.action in ['deposit','withdraw'] and go_back:
            self.action=''
            self.ask_user_for_account_action()
        elif self.name == 'back':
            self.action= ''
            self.ask_user_for_action()
        elif self.account_type_num in ['1','2','3','4'] and go_back:
            self.account_type_num=''
            self.choosingaccount()
        elif self.ask_user_for_action in ['register','login'] and go_back:
            self.ask_user_for_action=''
            self.ask_user_for_action()
        elif self.decision == 'quit' or self.action == 'quit' or self.account_type_num == 'quit' or self.ask_user_for_action == 'quit':
            self.quit()
       
    
    
    def deposit(self):
        self.get_amount_input()
        old_subclass_account_balance = 0
        print('Deposit Accepted')
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
            self.update_total_balance()
            print('Your total balance is ' + "%.2f" % database[self.customer_id]['Total Balance'] + '€')
            print(f'Your {self.account_type} balance is ' + "%.2f" % new_balance + '€')
        else:
            print('Insufficient funds. Unable to withdraw.')

           
        
    def get_amount_input(self):
        while True:  
            try:
                self.amount = int(input("Please enter a valid amount:\nOr '0' to go back! "))
                if self.amount < 0:
                    print("Amount needs to be a positive integer.\nOr '0' to go back!")
                else:
                    break
            except ValueError:
                print('Invalid input. Please enter an integer.')

    def returning(self):
        decision = ''
        while decision.lower() != 'yes' and decision.lower() != 'no':
               decision = input("Do you want to do another transaction? Yes/No:")
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
    
    
    
    def day_check(self):
        current_date = datetime.datetime.now()
        if current_date.day == 1:
            business_financial_boost_percentage()
        else:
            return

        
        
#    def day_check(self):
#        self.current_date_time = datetime.now()
#        self.daytoday = current_date_time.day
#        self.daytoday
#        if self.daytoday == 1:
#            print(f'{current_date_time.date()}')
#            break
#         else:
#            print(f'{current_date_time.date()}')
#            break
    
    
    
#    def count_day(self):
#        self.current_date = datetime.date.today()
#        self.days_count += 1
#        if self.days_count == 30:
#           self.days_count = 0

        
        
#    def business_financial_boost_percentage(self):
#        if self.daytoday == 1:
#             self.subclass_account_balance *= 1.2
#             break
#        else:
#           break
        
        
class CheckingAccount(Account):
    def __init__(self, customer_id, account_type, action, default_value):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance =database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        
        
        
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
        self.last_withdraw_date = None
        
        
        
    def count_withdrawls(self):
        self.withdrawls_times += 1  
        print (f' This is your: {self.withdrawls_times} withdrawl!')
        if self.withdrawls_times > 3 and self.days_count < 30:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            
            
    
    def calculate_the_presentage_of_last_day(self):
        value = database[self.customer_id]['accounts'][account_type]
        last_day_value =value + value*1/100
        last_day_value = database[self.customer_id]['accounts'][account_type]

        
        
    def day_check(self):
        if daystime.day().today == 1:
            super().financial_boost_percentage()
    
    
    
    def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()
  


    def withdraw(self):
        if datetime.now().day == 1 and (self.last_withdraw_date is None or self.last_withdraw_date.month != datetime.now().month):
            self.withdrawls_times = 0
        elif self.withdrawls_times < 3:
            #print(f"Withdrawal of {self.amount} € successful.")
            self.withdrawls_times += 1
            self.last_withdraw_date = datetime.now()
            super().withdraw()
            super().update_total_balance()
            self.action = ""
            super().returning()
        else:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            self. returning()


            
class DepositGuardAccount(Account):
    def __init__(self, customer_id, account_type, action, default_value):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance =database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        
        
        
    def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()

        
        
class BusinessAccount(Account):
     def __init__(self, customer_id, account_type, action, default_value,days_count):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance = database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
    
    
    
     def financial_boost_percentage(self):
        if datetime.datetime.now().day == 1:
            self.subclass_account_balance *= 1.2        
    
    
    
     def deposit(self):
        super().deposit()
        #self.financial_boost_percentage()
        self.action = ''
        super().returning()

        
        
     def withdraw(self):
        super().withdraw()
        super().update_total_balance()
        self.action = ''
        super().returning()
DoAction = Account()
DoAction.ask_user_for_action()



===========================================================================TEST1=================================================================
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



















=========================================================================================================TEST2==============================================================================================================
==========================================================================================================4/19==============================================================================================================
database = {}    

import csv
import ast

def csv_to_dict(csv_file):
    data_dict = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts = ast.literal_eval(row['accounts'])
            data_dict[row['uuid']] = {
                'name': row['name'],
                'tax_id': int(row['tax_id']),
                'Total Balance': int(row['Total Balance']),
                'accounts': accounts
            }
    return data_dict

database = csv_to_dict("OfficialDB.csv")      
database

import sys
import datetime
import uuid
import getpass
from datetime import datetime
import pandas as pd
import csv
import os


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
        self.bs_account = BusinessAccount
        self.account_type = ''
        self.action = ''
        self.amount = 0
        self.account_type_num = ''

    def initialize_sublcass_instances(self,customer_id,account_type,action,default_value,days_count,withdrawls_times):
        self.ck_account = CheckingAccount(customer_id,account_type,action,default_value)
        self.sv_account = SavingsAccount(customer_id,account_type,action,default_value,days_count,withdrawls_times)
        self.bs_account = BusinessAccount(customer_id,account_type,action,default_value,days_count)

    def ask_user_for_action(self):
        while self.action.lower() not in ['login','register','withdraw','deposit','return','quit']:
            self.action = input('Welcome to Python Bank!\nWould you like to login or register?')
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
            self.name = input("Provide a username or type 'back' in order to login!: ") 
            if self.name.lower() == 'back':
                self.back()
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
            #self.count_day()
            print(f'Welcome Mr/Mrs {self.name.title()}')
            print(f'Your unique ID is {self.customer_id} \nThis is also your password you can log in with to your bank account like your credit card!')
            print("Let's get started! For now, we create three different accounts for you:")
            print("Checking Account serve as versatile tools that allow individuals store funds and easily make transactions  ")
            print("Savings Accounts offer individuals a secure means to accumulate funds and earn interest")
            print("Business accounts accrue a 10% balance increase on the first day of every month.")
            self.show_account_info(True)      
            self.choosingaccount()
                  
    def login(self):
        
  #     database={}
#        csv_file = 'OfficialDB.csv'
#        database = self.csv_to_nested_dict(csv_file)
        while True:
            self.user_id = str(getpass.getpass('Hello, Please enter your user ID.\nIf you want to Register type Register.\nIf you want to Exit type Exit\n ID:  '))
            if self.user_id in database: #or user_id =='Register' or user_id == 'Exit':
                self.customer_id = self.user_id
                self.initialize_sublcass_instances(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times)
                print(f"Welcome Mr/Mrs {database[self.customer_id]['name']}, we are happy to see you again!")
                #print (database[self.customer_id]['Total Balance'].get[self.default_value])
                self.show_account_info(False)
                self.choosingaccount()
                break
    
        
    def quit(self):
        print("Thank you for using Python Bank. Have a nice day!")
        fieldnames = ['uuid','name','tax_id','Total Balance','accounts']
        with open('OfficialDB.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for random_number, inner_dict in database.items():
                row = {'uuid': random_number}
                row.update(inner_dict)
                writer.writerow(row)
                self.action = ''
                
        sys.exit
    
    def csv_to_nested_dict1(self,csv_file):
        database = {}
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_id = uuid.UUID(row['uuid'])
                name = row['name']
                tax_id = int(row['tax_id'])
                total_balance = int(row['Total Balance'])
                accounts = eval(row['accounts'])  # Αντιστοιχίστε το πεδίο ως λεξικό
                # Τώρα μπορείτε να χρησιμοποιήσετε τα δεδομένα για να αρχικοποιήσετε το database σας
                #database[customer_id] =account_details
                 #  {
                  #  'name': name,
                    #'tax_id': tax_id,
                    #'Total Balance': total_balance,
                    #'accounts': accounts}
                

        
    def choosingaccount(self):
        self.account_type_num = ''
        while self.account_type_num not in ['1','2','3']:
            print('--|---------------------|')
            print('1.|   Checking Account  |')
            print('--|---------------------|')
            print('2.|   Savings Account   |')
            print('--|---------------------|')
            print('3.|   Business Account  |')
            print('--|---------------------|')
            self.account_type_num = (input('Please choose between a number to get in corresponding account! '))
            self.ask_user_for_account_action()
  
    def show_account_info(self,register):
        print ('Account Details')
        if register :
            print (f'User ID: {self.customer_id} ----- You will need this to login!')
        else:
            print(self.customer_id)
            print(f"Name : {database[self.customer_id]['name']}")
            print(f"Tax ID: {database[self.customer_id]['tax_id']}")
            print(f"Your Total Account Balance is : {database[self.customer_id]['Total Balance']}"+'€')
            print(f"• Checking's Account Balance is : {database[self.customer_id]['accounts']['Checking Account']}" +'€')
            print(f"• Saving's Account Balance is : {database[self.customer_id]['accounts']['Savings Account']}"+'€')
            print(f"• Business's Account Balance is : {database[self.customer_id]['accounts']['Business Account']}"+'€')

    def ask_user_for_account_action(self):
        if self.account_type_num == "1":
            self.account_type = ('Checking Account')
            print('You are Currently in your Checking Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).deposit()
            elif self.action.lower() == 'withdraw':
                CheckingAccount(self.customer_id,self.account_type,self.action,self.default_value).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() == 'quit':
                self.quit()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
            #self.ck_account.ask_user_for_account_action()
        elif self.account_type_num == "2":
            self.account_type = ('Savings Account')
            print('Savings Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).deposit()
            elif self.action.lower() == 'withdraw':
                SavingsAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count,self.withdrawls_times).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() == 'quit':
                self.quit()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()
            #self.sv_account.ask_user_for_action()
        else:
            self.account_type = ('Business Account')
            print('Business Account')
            self.action = ''
            self.action = input('Do you want to deposit or withdraw. Press "back" if u willing to choose another account or "quit" to stop the process?')
            if self.action.lower() == "deposit":
                BusinessAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count).deposit()
            elif self.action.lower() == 'withdraw':
                BusinessAccount(self.customer_id,self.account_type,self.action,self.default_value,self.days_count).withdraw()
            elif self.action.lower() == 'back':
                self.back()
            elif self.action.lower() == 'quit':
                self.quit()
            elif self.action.lower() != 'deposit' or self.action.lower() != 'withdraw' or self.action !='back' or self.action != 'quit':                
                print('Please enter a valid action!')
                self.ask_user_for_account_action()   
            
    def back(self,go_back=True):
        
        if self.action in ['deposit','withdraw'] and go_back:
            self.action=''
            self.ask_user_for_account_action()
        
        if self.name == 'back':
            self.action= ''
            self.ask_user_for_action()
        
        #chose wrong action go back 1 step (account 1/2/3)
        elif self.account_type_num in ['1','2','3'] and go_back:
            self.account_type_num=''
            self.choosingaccount()

        elif self.ask_user_for_action in ['register','login'] and go_back:
            self.ask_user_for_action=''
            self.ask_user_for_action()

        elif self.decision == 'quit' or self.action == 'quit' or self.account_type_num == 'quit' or self.ask_user_for_action == 'quit':
            self.quit()
            
                  
    def deposit(self):
        self.get_amount_input()
        old_subclass_account_balance = 0
        print('Deposit Accepted')
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
            self.update_total_balance()
            print('Your total balance is ' + "%.2f" % database[self.customer_id]['Total Balance'] + '€')
            print(f'Your {self.account_type} balance is ' + "%.2f" % new_balance + '€')
        else:
            print('Insufficient funds. Unable to withdraw.')

            
    def get_amount_input(self):
            while True:
                self.amount = int(input("Please enter a valid amount:\nOr '0' to go back! "))
                if type(self.amount)!= int:
                    print("Amount cannot be alphanumeric.\nOr '0' to go back!")
                elif self.amount < 0:
                    print("Amount needs to be a positive integer.\nOr '0' to go back!")
                else:
                    break

    def returning(self):
        decision = ''
        while decision.lower() != 'yes' and decision.lower() != 'no':
               decision = input("Do you want to do another transaction? Yes/No:")
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
    
    def financial_boost_percentage(self):
        if daystime.now().day == 1:
            self.subclass_account_balance *= 1.1
    
        
class CheckingAccount(Account):
    def __init__(self, customer_id, account_type, action, default_value):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        print(f'Tο  4 O customer_id είναι: {self.customer_id}')
        self.subclass_account_balance =database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
        
        
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
        self.last_withdraw_date = None
        
    def count_withdrawls(self):
        self.withdrawls_times += 1  
        print (f' This is your: {self.withdrawls_times} withdrawl!')
        if self.withdrawls_times > 3 and self.days_count < 30:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            
    
    def calculate_the_presentage_of_last_day(self):
        value = database[self.customer_id]['accounts'][account_type]
        last_day_value =value + value*1/100
        last_day_value = database[self.customer_id]['accounts'][account_type]

    def day_check(self):
        if daystime.day().today == 1:
            super().financial_boost_percentage()
    
    def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()
  

    def withdraw(self):
        if datetime.now().day == 1 and (self.last_withdraw_date is None or self.last_withdraw_date.month != datetime.now().month):
            self.withdrawls_times = 0
        elif self.withdrawls_times < 3:
            #print(f"Withdrawal of {self.amount} € successful.")
            self.withdrawls_times += 1
            self.last_withdraw_date = datetime.now()
            super().withdraw()
            super().update_total_balance()
            self.action = ""
            super().returning()
        else:
            print('Withdrawal limit reached. Withdrawal functionality is locked.')
            self. returning()


            
            
class BusinessAccount(Account):
     def __init__(self, customer_id, account_type, action, default_value,days_count):
        super().__init__()
        self.customer_id = customer_id
        self.account_type = account_type
        self.action = action
        self.default_value = default_value
        self.subclass_account_balance = database[self.customer_id]['accounts'].get(self.account_type, self.default_value)
    
     def financial_boost_percentage(self):
            if daystime.now().day == 1:
                self.subclass_account_balance *= 1.1

     def deposit(self):
        super().deposit()
        self.action = ''
        super().returning()

     def withdraw(self):
        super().withdraw()
        super().update_total_balance()
        self.action = ''
        super().returning()
DoAction = Account()
DoAction.ask_user_for_action()



