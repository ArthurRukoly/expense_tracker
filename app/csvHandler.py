import os
import pandas as pd
from Transaction import Transaction

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class CSVHandler:

    def __init__(self, filename="text.csv"):
        self.filename = __location__ + "/../saves/" + filename
        try:
            self.data = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["Target", "Amount", "Balance"])
    
    def write_to_csv(self, transactions):
        transactions.to_csv(self.filename, mode='a', header=True, index=False)
    
    def load_from_csv(self):
        return pd.read_csv(self.filename)