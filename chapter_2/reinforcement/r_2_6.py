def make_payment(self, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError('amount must be numeric')
    elif amount < 0:
        raise ValueError('negative value was sent. amount must be positive')
    else:
        self._balance -= amount

