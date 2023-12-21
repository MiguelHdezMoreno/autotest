from flask import Flask, render_template
from bankaccount.bankaccount import BankAccount
import logging

app = Flask(__name__)

@app.route('/')
def home():
    my_account = BankAccount("Miguel Ángel")
    logging.info(my_account)
    my_account.show_balance()
    my_account.deposit(200)
    return render_template('index.html', account=my_account)

if __name__ == '__main__':
    app.run(debug=True)