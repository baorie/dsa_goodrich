def charge(self, price):
    if not isinstance(price, (int, float)):
        raise TypeError('price must be numeric')
    elif price + self._balance > self._limit:
        return False
    else:
        self._balance += price
        return True

def make_payment(self, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError('amount must be numeric')
    else:
        self._balance -= amount
