
#%%
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name}, {self.age}'
    def walk(self):
        return f'{self.name} is walking.'
    def noise(self):
        return f'{self.name} is making noise.'
    def eating(self):
        return f'{self.name} is eating. '

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def walk(self):
        return f'{self.name} is walking.'
    def noise(self):
        return f' dog is barking'

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def walk(self):
        return f'{self.name} is walking.'
    def noise(self):
        return f'{self.name} is meowing.'

class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def walk(self):
        return f'{self.name} is walking.'
    def noise(self):
        return f'{self.name} is neighing'

#%% md

#%%
import random
class Account():
    def __init__(self,account_number,name,balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def __str__(self):
        return f'{self.account_number}, {self.name}, {self.balance}'
class Bank():
    def __init__(self,accounts:dict):
        self.accounts = accounts
    def create_account(self,name,initial_balance):
        account_number=random.randint(1,100000)
        while account_number in self.accounts.keys():
            account_number=random.randint(1,100000)
        self.accounts[account_number] = Account(account_number,name,initial_balance)

    def view_account(self,account_number):
        try:
            return self.accounts[account_number]
        except KeyError:
            return f'there is no account number {account_number}'

    def deposit(self,amount,account_number):
        if amount>0:
            try:
                self.accounts[account_number].balance += amount
                return 'Updated'
            except KeyError:
                return f'there is no account number {account_number}'
        else:
            return 'Insufficient amount'

    def withdraw(self,amount,account_number):
        try:
            if amount>0:
                if self.accounts[account_number].balance < amount:
                    return f'Insufficient balance'
                else:
                    self.accounts[account_number].balance -= amount
                    return 'Withdrawn'
            else:
                return 'Insufficient amount'
        except KeyError:
            return f'there is no account number {account_number}'

    def save_to_file(self):
        with open('accounts.txt','w') as file:
            for account_number in self.accounts:
                file.write(str(f'{self.accounts[account_number].account_number},{self.accounts[account_number].name},{self.accounts[account_number].balance}\n'))

    def load_from_file(self):
        try:
            with open('accounts.txt') as file:
                for line in file:
                    acc_num,name,balance=line.strip().split(',')
                    account_number=int(acc_num)
                    balance=int(balance)
                    self.accounts[account_number] = Account(account_number,name,balance)
        except FileNotFoundError:
            pass


