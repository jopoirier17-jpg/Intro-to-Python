import random

class BankAccount:
    def __init__(self, username, accountType, balance=0):
        self._username = username
        self._accountType = accountType
        self._balance = balance
        # Generate a random 5-digit ID
        self._id = random.randint(10000, 99999)
        
        # Format: username_accountType_id.txt
        self.filename = f"{self._username}_{self._accountType}_{self._id}.txt"
        
        # Create the file and log the initial balance
        with open(self.filename, "w") as f:
            f.write(f"Statement for {self._username} ({self._accountType})\n")
            f.write(f"Account ID: {self._id}\n")
            f.write(f"Initial Balance: {self._balance}\n")
            f.write("-" * 30 + "\n")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction(f"Deposited: +{amount} | New Balance: {self._balance}")
            print(f"Deposited {amount}. Current balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds! Attempted to withdraw {amount}, but current balance is {self._balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            self._log_transaction(f"Withdrew: -{amount} | New Balance: {self._balance}")
            print(f"Withdrew {amount}. Current balance: {self._balance}")

    def get_balance(self):
        return self._balance

    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def get_account_type(self):
        return self._accountType

    def get_transaction_history(self):
        print(f"\n--- History for {self.filename} ---")
        try:
            with open(self.filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return "Transaction file not found."

    def _log_transaction(self, message):
        with open(self.filename, "a") as f:
            f.write(message + "\n")


# 1. Create 3 users account
user1 = BankAccount("RoboGarden", "checking", 500)
user2 = BankAccount("John", "saving") # Balance defaults to 0
user3 = BankAccount("Stephany", "Checking", 2000)

# 2. Perform transactions for Robogarden
user1.deposit(200)
user1.withdraw(100)
user1.withdraw(1000) # Should fail (insufficient funds)

# 3. Perform transactions for John
user2.deposit(1000)
user2.withdraw(250)

# 4. Retrieve data
print(f"\nUser: {user1.get_username()} | ID: {user1.get_id()} | Type: {user1.get_account_type()}")
print(f"Current Balance for {user1.get_username()}: {user1.get_balance()}")

# 5. Get transaction history from file
print(user1.get_transaction_history())
print(user2.get_transaction_history())
print(user3.get_transaction_history())
