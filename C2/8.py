# R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?

import code
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, bonus):
        """Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._bonus = bonus
        self._balance = 0 + self._bonus


    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        try:
            price = int(price)
            if price + self._balance > self._limit:  # if charge would exceed limit,
                print "Charge for %s denied. Reached limit on card %s." % (self._balance, self._bank)
                return False  # cannot accept charge
            else:
                self._balance += price
                print "Charge for %s approved. Current balance owed on card is %s." % (self._balance, self._bank)
                #return true
        except(ValueError, TypeError) as e:
            print("You've entered a non numeric value. Please try again.\n Error Code -> '%s'" % e)

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if amount>0:
            try:
                self._balance -= float(amount)
            except ValueError as e:
                print("You've entered a non numeric value. Please try again.\n Error Code -> '%s'" % e)
        else:
            raise TypeError('A non acceptable input was entered. Please enter a positive amount.')


#This function multiplies all cards by a random int between 1 and 17. It will alw
def random_charges(wallet):
    if True:
    # while True:
        for val in range(1, 17):
            wallet[0].charge(val)
            wallet[1].charge(2 * val)
            wallet[2].charge(3 * val)
    code.interact(local=locals())

def main():
    # cc = CreditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000, bonus)
    while True:
        try:
            bonus = raw_input("Would you like to enter a bonus/charge opening value?\nIf yes, enter an amount. If you do not wish to open with a balance, please enter [N], [n], or [0]. ")
            if bonus == 'N' or bonus == 'n' or bonus == '' or bonus == ' ' or bonus == '0':
                print 'No opening credit will be assigned to this account.'
                bonus = 0
                break
            elif float(bonus):
                bonus = float(bonus)
                break
            else:
                print(
                    "Value not accepted. \n If you do not wish to open with a balance, please enter\n [N], [n], or [0]. ")
        except ValueError or TypeError:
            print ("Value not accepted. \n If you do not wish to open with a balance, please enter\n [N], [n], or [0]. ")

    # print type(bonus)
    # print bonus
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings',
                             '5391 0375 9387 5309', 2500, bonus))
    wallet.append(CreditCard('John Bowman', 'California Federal',
                             '3485 0399 3395 1954', 3500, bonus))
    wallet.append(CreditCard('John Bowman', 'California Finance',
                             '5391 0375 9387 5309', 5000, bonus))
    random_charges(wallet)
    # while True:
    #     random_charges(wallet) == True

main()