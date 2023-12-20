import logging
logging.basicConfig(filename='bankaccount.log', level=logging.INFO, encoding='utf-8', format='%(message)s')  # Remove the timestamp from the log message

class BankAccount(object):
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def __repr__(self):
        return "%s's account. Balance: %.2f€" % (self.name, self.balance)

    def show_balance(self):
        logging.info("Balance: %.2f€" % self.balance)

    def deposit(self, amount):
        if amount <= 0:
            logging.error("Your deposit must be greater than 0")
            return
        else:
            logging.info("Your deposit consists of %.2f€" % amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error("You do not have enough withdrawal power")
            return
        else:
            logging.info("You have taken %.2f€" % amount)
            self.balance -= amount
            self.show_balance()

my_account = BankAccount("Miguel Ángel")
logging.info(my_account)
my_account.show_balance()
my_account.deposit(200)
my_account.withdraw(50)