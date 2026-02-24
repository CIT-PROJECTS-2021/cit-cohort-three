import json
from dataclasses import dataclass, asdict
from pathlib import Path

DATA_FILE = Path("bank_data.json")


class BankingError(Exception):
    pass


class InsufficientFundsError(BankingError):
    pass


class AccountNotFoundError(BankingError):
    pass


@dataclass
class Account:
    account_id: str
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount


class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id: str, owner: str, balance: float) -> Account:
        if account_id in self.accounts:
            raise BankingError("Account ID already exists.")
        account = Account(account_id=account_id, owner=owner, balance=balance)
        self.accounts[account_id] = account
        return account

    def get_account(self, account_id: str) -> Account:
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account not found.")
        return self.accounts[account_id]

    def transfer(self, from_id: str, to_id: str, amount: float) -> None:
        sender = self.get_account(from_id)
        receiver = self.get_account(to_id)
        sender.withdraw(amount)
        receiver.deposit(amount)

    def to_dict(self) -> dict:
        return {"accounts": [asdict(a) for a in self.accounts.values()]}

    @staticmethod
    def from_dict(data: dict) -> "Bank":
        bank = Bank()
        for item in data.get("accounts", []):
            account = Account(**item)
            bank.accounts[account.account_id] = account
        return bank


def load_bank() -> Bank:
    if not DATA_FILE.exists():
        return Bank()
    try:
        data = json.loads(DATA_FILE.read_text())
        return Bank.from_dict(data)
    except (json.JSONDecodeError, OSError):
        return Bank()


def save_bank(bank: Bank) -> None:
    DATA_FILE.write_text(json.dumps(bank.to_dict(), indent=2))


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            return value
        except ValueError:
            print("Please enter a valid number.")


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def menu() -> None:
    bank = load_bank()
    actions = {
        "1": "Create account",
        "2": "Deposit",
        "3": "Withdraw",
        "4": "Transfer",
        "5": "Check balance",
        "6": "List accounts",
        "0": "Exit",
    }

    while True:
        print("\n=== Banking Console ===")
        for key, label in actions.items():
            print(f"{key}. {label}")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                account_id = read_non_empty("Account ID: ")
                owner = read_non_empty("Owner name: ")
                balance = read_float("Starting balance: ")
                account = bank.create_account(account_id, owner, balance)
                save_bank(bank)
                print(f"Account created for {account.owner}.")
            elif choice == "2":
                account_id = read_non_empty("Account ID: ")
                amount = read_float("Deposit amount: ")
                bank.get_account(account_id).deposit(amount)
                save_bank(bank)
                print("Deposit successful.")
            elif choice == "3":
                account_id = read_non_empty("Account ID: ")
                amount = read_float("Withdrawal amount: ")
                bank.get_account(account_id).withdraw(amount)
                save_bank(bank)
                print("Withdrawal successful.")
            elif choice == "4":
                from_id = read_non_empty("From account ID: ")
                to_id = read_non_empty("To account ID: ")
                amount = read_float("Transfer amount: ")
                bank.transfer(from_id, to_id, amount)
                save_bank(bank)
                print("Transfer successful.")
            elif choice == "5":
                account_id = read_non_empty("Account ID: ")
                account = bank.get_account(account_id)
                print(f"Balance: {account.balance:.2f}")
            elif choice == "6":
                if not bank.accounts:
                    print("No accounts found.")
                for account in bank.accounts.values():
                    print(
                        f"{account.account_id} | {account.owner} | {account.balance:.2f}"
                    )
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Invalid option.")
        except BankingError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    menu()
