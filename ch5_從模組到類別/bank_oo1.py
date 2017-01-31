# encoding:utf8

class Account:

    def __init__(self,name,number,balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

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
    acct = Account(name ='ihong',number=879487,balance=1000)
    print(acct)
    acct.deposit(-100)
    acct.deposit(100)

    print(acct.__balance) ## 不能存取私有屬性
    print(acct)
