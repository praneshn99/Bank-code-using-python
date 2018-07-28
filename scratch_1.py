class Account:
    counter = 0

    def __init__(self,balance=0):
        self.__balance = balance           # A double underscore encrypts the object from user
        self.id = Account.counter          #  Known as Name mangling
        Account.counter += 1
        self.trans = 0
        self.max_trans = 2

    def deposit(self,amount):
        if amount > 0 and self.trans < self.max_trans :
           self.__balance += amount
           self.trans += 1


    def get_balance(self):
        return self.__balance


    def deposit_interest(self,amount):
        self.__balance += amount


    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance and self.trans < self.max_trans:
               self.__balance -= amount
               self.trans += 1
        else:
            print('Invalid transaction')

    def __str__(self):
        return f'The Account number 52986600{Account.counter} has available balance of {self.get_balance()} Rs. '



print('For Savings Account type - SA')
print('For Current Account type - CA')
access = input('Which account do you want to access? Type here ->  ')

if access == 'SA':
    class SavingsAccount(Account):
        def get_interest(self):
            return self.deposit_interest(self.get_balance() * 0.06)



    print('Welcome customer')
    sa1 = SavingsAccount(int(input('Enter opening balance: ')))
    print('For deposit press D')
    print('For Withdrawal press W')
    option = input('Option: ')
    if option == 'D':
        sa1.deposit(int(input('Enter the amount to be deposited: ')))
    elif option == 'W':
        sa1.withdraw(int(input('Enter the amount withdrawn: ')))
    else:
        print('Try again')
        print('For deposit press D')
        print('For Withdrawal press W')
        option = input('Option: ')
        if option == 'D':
            sa1.deposit(int(input('Enter the amount to be deposited: ')))
        elif option == 'W':
            sa1.withdraw(int(input('Enter the amount withdrawn: ')))
        else:
            print('Last Try! Fill carefully!')
            print('For deposit press D')
            print('For Withdrawal press W')
            option = input('Option: ')
            if option == 'D':
                sa1.deposit(int(input('Enter the amount to be deposited: ')))
            elif option == 'W':
                sa1.withdraw(int(input('Enter the amount withdrawn: ')))
            else:
                print('Transaction cancelled.(INFO : Invalid Option) ')

    print(sa1)
    print('Thank You! Visit Again')
    print('-X' * 30 + '-')

elif access == 'CA':
    class CurrentAccount(Account):

        def __init__(self):
            super()  # It helps in referencing to the super class of the sub class being used.
            self.max_trans = 3


    print('Welcome customer')
    ca1 = Account(int(input('Enter the amount: ')))
    print('For deposit press D')
    print('For Withdrawal press W')
    option = input('Option: ')
    if option == 'D':
        ca1.deposit(int(input('Enter the amount to be deposited: ')))
    elif option == 'W':
        ca1.withdraw(int(input('Enter the amount withdrawn: ')))
    else:
        print('Try again')
        print('For deposit press D')
        print('For Withdrawal press W')
        option = input('Option: ')
        if option == 'D':
            ca1.deposit(int(input('Enter the amount to be deposited: ')))
        elif option == 'W':
            ca1.withdraw(int(input('Enter the amount withdrawn: ')))
        else:
            print('Last Try! Fill carefully!')
            print('For deposit press D')
            print('For Withdrawal press W')
            option = input('Option: ')
            if option == 'D':
                ca1.deposit(int(input('Enter the amount to be deposited: ')))
            elif option == 'W':
                ca1.withdraw(int(input('Enter the amount withdrawn: ')))
            else:
                print('Transaction cancelled.(INFO : Invalid Option) ')

    print(ca1)
    print('Thank You! Visit Again')
    print('-X' * 30 + '-')

else:
    print('Invalid option! Try Again')
