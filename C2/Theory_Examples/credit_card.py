# print card
# <__main__.credit_card instance at 0x00912AD0>
# >>> print type(card)
# <type 'instance'>
# >>> print card.get_customer()
# shawn

import code
class credit_card:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limt = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

def main():
    customer = raw_input('Please enter your name:\n')
    bank = raw_input('Please enter your bank company:\n')
    account = raw_input('Please enter your account number:\n')
    limit = raw_input('Please enter your limit:\n')
    balance = raw_input('Please enter your current balance:\n')
    card = credit_card(customer,bank,account,limit)

    code.interact(local = locals())
main()

