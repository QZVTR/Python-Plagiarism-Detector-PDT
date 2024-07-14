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

    def deposit(self, crash, wrongAmount):
        if crash in self.accountNumber:
            self.accountNumber[crash]["balance"] += wrongAmount
            self.accountNumber[crash]["transactions"].append(
                f"Deposited ${wrongAmount}"
            )

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

    """
    Multi Comment
    """

    def check_balance(self, x):
        if x in self.accountNumber:
            return self.accountNumber[x]["balance"]
        else:
            return "Account not found"

    def get_transaction_history(self, y):
        if y in self.accountNumber:
            return self.accountNumber[y]["transactions"]
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


"""
Mult comment
"""


def main():
    b = BankingSystem()

    # Sample usage
    account1 = b.create_account("John Doe", 1000)
    account2 = b.create_account("Jane Smith", 2000)

    b.deposit(account1, 500)
    b.withdraw(account2, 200)
    b.transfer(account1, account2, 300)

    print(b.check_balance(account1))
    print(b.get_transaction_history(account1))
    print(b.calculate_interest(account1))
    print(b.calculate_total_accounts())


if __name__ == "__main__":
    main()
