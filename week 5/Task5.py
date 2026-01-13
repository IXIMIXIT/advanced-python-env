class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner = owner       # Private attribute
        self.__balance = initial_balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

# Demonstration
if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200) # Should fail
    
    # Trying to access private variable directly (will fail or cause error)
    # print(account.__balance) # Uncommenting this line raises an AttributeError
    
    print(f"Final Balance for {account._BankAccount__owner}: ${account.get_balance()}")