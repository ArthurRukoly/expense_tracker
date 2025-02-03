import pandas as pd

class CSVHandler:
    def __init__(self, filename="text.csv"):
        self.filename = filename
        try:
            self.data = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["Target", "Amount", "Balance"])
    
    def write_to_csv(self, transactions):
        transactions.to_csv(self.filename, mode='a', header=False, index=False)
    
    def load_from_csv(self):
        return pd.read_csv(self.filename)