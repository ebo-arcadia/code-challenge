# To raise an exception, you can use the 'raise' keyword.
# Note that you can only raise an object of the Exception class or its subclasses.
# Exception is an inbuilt class in python.
# To raise subclasses of Exception(custom Exception) we have to create our own custom Class.
# We can also pass message along with exception so that exception handling is consistent.


class Consumer:
    def __init__(self, payment):
        self.payment = payment
        self.lowest_budget = 100
        self.highest_budget = 1000


class Seller:
    def sell_goods_or_services(self, consumerA):
        if consumerA.payment < consumerA.lowest_budget:
            raise LowerThanBudgetException(consumerA)
        elif consumerA.payment > consumerA.highest_budget:
            raise HigherThanBudgetException(consumerA)
        else:
            print("great price")
            return "price is within the budget"


class LowerThanBudgetException(Exception):
    def __init__(self, consumerA):
        message = "the selling price is: " \
                  + str(consumerA.payment) \
                  + " which is too LOW. " \
                  + "find a price between: " \
                  + str(consumerA.lowest_budget) + " and " + str(consumerA.highest_budget)
        super().__init__(message)


class HigherThanBudgetException(Exception):
    def __init__(self, consumerA):
        message = "the selling price is: " \
                  + str(consumerA.payment) \
                  + " which is too HIGH. " \
                  + "find a price between: " \
                  + str(consumerA.lowest_budget) + " and " + str(consumerA.highest_budget)
        super().__init__(message)


try:
    entered_price = input("please enter a price: ")
    consumerA = Consumer(int(entered_price))
    sellerA = Seller()
    sellerA.sell_goods_or_services(consumerA)
except LowerThanBudgetException as lower_e:
    print(lower_e)
except HigherThanBudgetException as higher_e:
    print(higher_e)