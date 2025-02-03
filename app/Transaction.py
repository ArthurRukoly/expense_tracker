import pandas as pd

class Transaction:
    def __init__(self, balance):
        self.transactions = pd.DataFrame(columns=["Target", "Amount", "Balance"])
        self.balance = balance
    
    def add_transaction(self, target, amount):
        self.balance += amount 
        new_transaction = pd.DataFrame({
            "Target": [target],
            "Amount": [amount],
            "Balance": [self.balance]
        })
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
    
    def display_transactions(self):
        print(self.transactions)

    def summarize_by_target(self):
        summary = self.transactions.groupby("Target", as_index=False)["Amount"].sum()
        print(summary)

    def import_csv(self, csv):
        data = pd.read_csv(csv)
        self.transactions = pd.concat([self.transactions, data], ignore_index=True)

    def import_transaction(self, imported_transactions):
        for transaction in imported_transactions:
            self.add_transaction(transaction["Target"], transaction["Amount"])