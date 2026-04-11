class BankAccount:
    def __init__(self):
        self._is_open = False
        self._balance = 0

    def get_balance(self):
        if self._is_open:
            return self._balance 
        else:
            raise ValueError('account not open')

    def open(self):
        if self._is_open:
            raise ValueError('account already open')
        self._is_open = True
        self._balance = 0
        
    def deposit(self, amount):
        if self._is_open:
            if amount > 0:
                self._balance += amount
            else:
                raise ValueError('amount must be greater than 0')
        else:
            raise ValueError('account not open')

    
    def withdraw(self, amount):
        if self._is_open:
            if amount > self._balance:
                raise ValueError('amount must be less than balance')
            elif amount > 0:
                self._balance -= amount
            else:
                raise ValueError('amount must be greater than 0')
        else:
            raise ValueError('account not open')
            

    def close(self):
        if self._is_open:
            self._is_open = False
        else:
            raise ValueError('account not open')

