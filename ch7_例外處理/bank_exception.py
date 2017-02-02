#! encoding:utf8
class Account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance

    def check_amount(self,amount):
        if amount <=0 :
            raise ValueError('金額必須為正數:'+ str(amount))

    def deposit(self,amount):
        self.check_amount(amount)
        self.balance += amout

    def withdraw(self,amount):
        self.check_amount(amount)
        if amount > self.balance:
            # raise 
            raise BankingException('餘額不足')
        self.balance -= amount

    def __str__(self):
        return "Account('{name}','{number}',{balance})".format(
            **vars(self)
        )

class BankingException(Exception):
    def __init__(self,message):
        super().__init__(message)

if __name__ == '__main__':
    jack = Account('Jack','100-1011',5000)
    print(jack)
    jack.withdraw(900)
    print(jack)

    ## 紀錄error log
    try:
        jack.deposit(-500)
    except ValueError as err:
        import logging, datetime
        logging.getLogger(__name__).log(
            logging.ERROR,
            'Error Logging:{time}, {number}, {message}'.format(
                time = datetime.datetime.now(),
                number = jack.number,
                message = err
            )
        )
        # raise

        ## 自定義
        raise BankingException('輸入金額為負的行為已紀錄') from err

    try:
        jack.withdraw(50000)
    except BankingException as err:
        print(err)
