class Account:
    def __init__(self, customer_id, account_nbr):
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0

    def get_customer_id(self):
        return self._customer_id

    def get_account_nbr(self):
        return self._account_nbr

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return (
            f'Account(owner: {self._customer_id}, '
            f'nbr: {self._account_nbr}, '
            f'balance: {self._balance})'
        )


    def __repr__(self):
        return str(self)

class Bank:
    def __init__(self):
        self._customers = {}
        self._accounts = {}
        self._next_customer_id = 1
        self._next_account_nbr = 1

    def add_customer(self, name):
        customer_id = 'C' + str(self._next_customer_id)
        self._customers[customer_id] = name
        self._next_customer_id += 1
        return customer_id

    def get_customer_name(self, customer_id):
        return self._customers.get(customer_id)

    def create_account(self, customer_id):
        if customer_id in self._customers:
            account_nbr = self._next_account_nbr
            self._accounts[account_nbr] = Account(customer_id, account_nbr)
            self._next_account_nbr += 1
            return account_nbr
        else:
            return -1

    def get_account(self, account_nbr):
        return self._accounts.get(account_nbr)

    def accounts_by_customer(self, customer_id):
        accounts = []
        for account in self._accounts.values():
            if account.get_customer_id() == customer_id:
                accounts.append(account)
        return accounts

    def remove_account(self, account_nbr):
        account = self._accounts.get(account_nbr)
        if account is not None and account.get_balance() == 0:
            del self._accounts[account_nbr]
            return True
        else:
            return False

    def transfer(self, from_account_nbr, to_account_nbr, amount):
        from_account = self._accounts.get(from_account_nbr)
        to_account = self._accounts.get(to_account_nbr)
        if from_account is None or to_account is None:
            return False
        elif from_account.get_balance() < amount:
            return False
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            return True

    def total_balances(self):
        return sum(account.get_balance() for account in self._accounts.values())

    def all_accounts(self):
        return list(self._accounts.values())

    def all_accounts_sorted_by_balance(self):
        return sorted(self._accounts.values(), key=lambda account: account.get_balance(), reverse=True)

