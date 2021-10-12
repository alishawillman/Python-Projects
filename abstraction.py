


from abc import ABC, abstractmethod
class tv(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    #function passing an argument
        @abstractmethod
        def payment(self, amount):
            pass

class OnlinePayment(tv):
    #defining how to implement the payment function
    def payment(slef, amount):
        print('Your purchase amount of {} exceeded your $500 limit '.format(amount))

obj = OnlinePayment()
obj.paySlip("$699")
obj.payment("$699")
