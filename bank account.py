class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} successful.")
            print(f"New balance: ${self.__balance}")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount

            print(f"Withdrawal of ${amount} successful.")
            print(f"New balance: ${self.__balance}")

        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance


# Savings class inherits from Account
class Savings(Account):

    def __init__(self, owner, balance=0):

        # Call parent constructor
        super().__init__(owner, balance)

        # Interest rate
        self.interest_rate = 0.02

        # Withdrawal limit
        self.withdraw_limit = 100

    # Overriding withdraw method
    def withdraw(self, amount):

        # Check withdrawal limit
        if amount > self.withdraw_limit:
            print(f"Withdrawal cannot be more than ${self.withdraw_limit}")

        else:
            # Use parent withdraw method
            super().withdraw(amount)

    def apply_interest(self):

        interest = self.get_balance() * self.interest_rate

        self.deposit(interest)

        print(f"Interest of ${interest} applied.")


# ===== TESTING THE PROGRAM =====

print("------ Savings Account ------")

savings = Savings("Alice", 1000)

print(f"Initial balance: ${savings.get_balance()}")

print("\nDepositing Money")
savings.deposit(500)

print("\nWithdrawal within limit")
savings.withdraw(80)

print("\nWithdrawal above limit")
savings.withdraw(200)

print("\nApplying Interest")
savings.apply_interest()

print(f"\nFinal balance: ${savings.get_balance()}")