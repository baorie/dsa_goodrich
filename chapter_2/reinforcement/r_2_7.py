class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
