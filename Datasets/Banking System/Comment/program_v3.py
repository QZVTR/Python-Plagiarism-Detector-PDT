class BankingSystem:
    def __init__(self):
        self.accounts = {}

    # Comment 1
    def create_account(self, name, balance):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = {
            "name": name,
            "balance": balance,
            "transactions": [],
        }
        return account_number

    # Comment 2
    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions"].append(f"Deposited ${amount}")

    def withdraw(self, account_number, amount):
        if (
            account_number in self.accounts
            and self.accounts[account_number]["balance"] >= amount
        ):
            self.accounts[account_number]["balance"] -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrew ${amount}")

    def transfer(self, sender_account, receiver_account, amount):
        if (
            sender_account in self.accounts
            and receiver_account in self.accounts
            and self.accounts[sender_account]["balance"] >= amount
        ):
            self.accounts[sender_account]["balance"] -= amount
            self.accounts[receiver_account]["balance"] += amount
            self.accounts[sender_account]["transactions"].append(
                f"Transferred ${amount} to account {receiver_account}"
            )
            self.accounts[receiver_account]["transactions"].append(
                f"Received ${amount} from account {sender_account}"
            )

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["balance"]
        else:
            return "Account not found"

    def get_transaction_history(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["transactions"]
        else:
            return "Account not found"

    def calculate_interest(self, account_number):
        if account_number in self.accounts:
            # Placeholder logic for interest calculation
            return 0.05 * self.accounts[account_number]["balance"]  # 5% interest rate
        else:
            return "Account not found"

    def calculate_total_accounts(self):
        return len(self.accounts)


def main():
    bank = BankingSystem()

    # Sample usage
    account1 = bank.create_account("John Doe", 1000)
    account2 = bank.create_account("Jane Smith", 2000)

    bank.deposit(account1, 500)
    bank.withdraw(account2, 200)
    bank.transfer(account1, account2, 300)

    print(bank.check_balance(account1))
    print(bank.get_transaction_history(account1))
    print(bank.calculate_interest(account1))
    print(bank.calculate_total_accounts())


if __name__ == "__main__":
    main()
