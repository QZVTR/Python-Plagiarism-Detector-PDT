class BankingSystem:
    def __init__(self):
        self.accountNumber = {}

    def create_account(self, n, b):
        account = len(self.accountNumber) + 1
        self.accountNumber[account] = {
            "name": n,
            "balance": b,
            "transactions": [],
        }
        return account

    def close_account(self, a):
        if a in self.accountNumber:
            del self.accountNumber[a]

    def deposit(self, account_number, amount):
        if account_number in self.accountNumber:
            self.accountNumber[account_number]["balance"] += amount
            self.accountNumber[account_number]["transactions"].append(
                f"Deposited ${amount}"
            )

    def withdraw(self, account_number, amount):
        if (
            account_number in self.accountNumber
            and self.accountNumber[account_number]["balance"] >= amount
        ):
            self.accountNumber[account_number]["balance"] -= amount
            self.accountNumber[account_number]["transactions"].append(
                f"Withdrew ${amount}"
            )

    def transfer(self, sender_account, receiver_account, amount):
        if (
            sender_account in self.accountNumber
            and receiver_account in self.accountNumber
            and self.accountNumber[sender_account]["balance"] >= amount
        ):
            self.accountNumber[sender_account]["balance"] -= amount
            self.accountNumber[receiver_account]["balance"] += amount
            self.accountNumber[sender_account]["transactions"].append(
                f"Transferred ${amount} to account {receiver_account}"
            )
            self.accountNumber[receiver_account]["transactions"].append(
                f"Received ${amount} from account {sender_account}"
            )

    def check_balance(self, account_number):
        if account_number in self.accountNumber:
            return self.accountNumber[account_number]["balance"]
        else:
            return "Account not found"

    def get_transaction_history(self, account_number):
        if account_number in self.accountNumber:
            return self.accountNumber[account_number]["transactions"]
        else:
            return "Account not found"

    def calculate_interest(self, account_number):
        if account_number in self.accountNumber:
            # Placeholder logic for interest calculation
            return (
                0.05 * self.accountNumber[account_number]["balance"]
            )  # 5% interest rate
        else:
            return "Account not found"

    def calculate_total_accounts(self):
        return len(self.accountNumber)


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
