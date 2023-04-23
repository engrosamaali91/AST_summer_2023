from abc import ABC, abstractmethod
# from datetime import date
# from enum import Enum

class Payment(ABC):
    @abstractmethod
    def __init__(self, amount: float):
        self.amount = amount
        
class Cash(Payment):
    def __init__(self, amount: float):
        
        super().__init__(amount)
    def tender_cash(self):
        self.__cash_tendered = float(input("enter the number"))
    def return_change(self):
        self.money = self.__cash_tendered - self.amount
        return self.money
    
    def __str__(self) -> str:
        printing = "\nReceipt \nCash Paid : {} \nChange returned : {}\n".format(self.__cash_tendered, self.return_change())
        return printing
    


c = Cash(1.1,2.2)
c.tender_cash()
