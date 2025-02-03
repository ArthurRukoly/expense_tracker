from Transaction import Transaction
from transactions import transactions


if __name__ == "__main__":

    app = Transaction(632)

    for transcation in transactions:
            app.add_transaction(transcation["Target"], transcation["Amount"])
    
    app.display_transactions()
    app.summarize_by_target()