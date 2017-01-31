# encoding:utf8

class Account:

    def __init__(self,name,number,balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @staticmethod
    def default(name,number):
        return Account(name,number,100)

    def deposit(self,amount):
        if amount <= 0:
            print('存款金額不能為負數，你數學比我家小屁孩還差。')
        else:
            self.__balance += amount
    def withdraw(self,amount):
        if amount > self.__balance:
            print('存款不夠你提，北七！')
        else:
            self.__balance -= amount

    def __str__(self):
        return "Account('{name}','{number}','{balance}')".format(
                name=self.__name,number=self.__number,balance=self.__balance)


if __name__ == '__main__':
    acct = Account('iddhong','1234',1000)
    print(acct.default('Monica','10-dd00'))
    # acct = Account(name ='ihong',number=879487,balance=1000)
    # print(str(acct))
    # acct.deposit(-100)
    # acct.deposit(100)
    # print(str(acct))
    # print(acct.__balance) ## 不能存取私有屬性
    # print('拿到私有屬性,name:{name},number:{number},balance:{balance}'.format(name=acct.name,number=acct.number,
                                        # balance = acct.balance))
