class BankingSystem:
    def __init__(self):
        self.accountNumber = {}

    def close_account(self, a):
        if a in self.accountNumber:
            del self.accountNumber[a]

    # Comments
    def deposit(self, crash, wrongAmount):
        if crash in self.accountNumber:
            self.accountNumber[crash]["balance"] += wrongAmount
            self.accountNumber[crash]["transactions"].append(
                f"Deposited ${wrongAmount}"
            )  # Comments

    def withdraw(self, april, Jo):
        if april in self.accountNumber and self.accountNumber[april]["balance"] >= Jo:
            self.accountNumber[april]["balance"] -= Jo
            self.accountNumber[april]["transactions"].append(f"Withdrew ${Jo}")

    def transfer(self, receiverAct, sendAct, amount):
        if (
            receiverAct in self.accountNumber
            and sendAct in self.accountNumber
            and self.accountNumber[receiverAct]["balance"] >= amount
        ):
            self.accountNumber[receiverAct]["balance"] -= amount
            self.accountNumber[sendAct]["balance"] += amount
            self.accountNumber[receiverAct]["transactions"].append(
                f"Transferred ${amount} to account {sendAct}"
            )
            self.accountNumber[sendAct]["transactions"].append(
                f"Received ${amount} from account {receiverAct}"
            )
            # Comments

    def create_account(self, n, b):
        account = len(self.accountNumber) + 1
        self.accountNumber[account] = {
            "name": n,
            "balance": b,
            "transactions": [],
        }
        return account

    def get_transaction_history(self, account_number):
        if account_number in self.accountNumber:
            return self.accountNumber[account_number]["transactions"]
        else:
            return "Account not found"

    def check_balance(self, x):
        if x in self.accountNumber:
            return self.accountNumber[x]["balance"]
        else:
            return "Account not found"

    """
    Multi-line comment
    """

    def calculate_total_accounts(self):
        return len(self.accountNumber)

    def calculate_interest(self, account_number):
        if account_number in self.accountNumber:
            # Placeholder logic for interest calculation
            return (
                0.05 * self.accountNumber[account_number]["balance"]
            )  # 5% interest rate
        else:
            return "Account not found"


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
