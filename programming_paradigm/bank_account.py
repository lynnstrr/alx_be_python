class BankAccount:
    """A simple bank account class that supports basic operations."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self._account_balance = initial_balance  # private balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance}")