from Transaction import Transaction
from transactions import transactions
from csvHandler import CSVHandler

csv = CSVHandler("DB")
app = Transaction(632)

if __name__ == "__main__":

#     app.import_transaction(transactions)
    app.import_csv(csv.filename)
#     csv.write_to_csv(app.transactions)
#     print(csv.load_from_csv())


    app.display_transactions()
    app.summarize_by_target()