# Use the techniques of Section 1.7 to revise the charge and make_payment methods of the CreditCard class to ensure that the caller sends a number as a parameter.
# If the parameter to the make_payment method of the CreditCard class were a negative number, that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative value is sent.
# The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter constructor syntax should continue to produce an account with zero balance.

class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit, balance = 0) -> None:
        """Creates a new credit card balance
        
        customer    the name of the customer (e.g. 'John Bowman')
        bank        the name of the bank (e.g. 'California Savings')
        acnt        the account identifier (e.g. '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Returns names of the customer"""
        return self._customer

    def get_bank(self):
        """Returns the bank's name"""
        return self._bank

    def get_account(self):
        """Returns the card identifying number (typically stored as a string)"""
        return self._acnt

    def get_limit(self):
        """Returns current credit limit"""
        return self._limit

    def get_balance(self):
        """Returns current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        
        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int,float)):
            raise TypeError('price must be a number')

        if price + self._balance > self._limit:  # if charge would exceed the limit,
            return False                         # cannot accept charge
        else: 
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces the balance"""
        if not isinstance(amount, (int,float)):
            raise TypeError('amount must be a number')
        elif amount < 0:
            raise ValueError('amount must be a positive number')
        
        self._balance -= amount

# Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3, so that it will eventually cause exactly one of the three credit cards to go over its credit limit. Which credit card is it? 
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Max', 'CIC', '8769 3477 5620 9832', 1000))
    wallet.append(CreditCard('Mat', 'BNP', '9269 3477 1120 9832', 2000))
    wallet.append(CreditCard('Marc', 'HSBC', '1669 3477 1120 9832', 2500))

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print('Customer =', wallet[c].get_customer())
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print('Balance =', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New balance =', wallet[c].get_balance())
    print()
