class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to the withdrawal and deposit machine")

    def accountnumber(self):
        accountnumber=float(input("Enter your account number:"))
        print("\nAccount number:",accountnumber)
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance+= amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
            amount = float(input("Enter amount to be Withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                print("\n You Withdrew:", amount)
            else:
                print("\n Insufficient balance  ")

    def display(self):
            print("\n Net Available Balance=", self.balance)


s = Bank_Account()
s.accountnumber()
s.deposit()
s.withdraw()
s.display()
