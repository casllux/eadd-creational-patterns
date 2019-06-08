from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """ The abstract factory class for defining the abstract methods the child classes should inherit.
        This class describes the different factory classes that allow for objects of their respective type to be create."""
        
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getLogin(self, login):
        pass
    
    @abstractmethod
    def getPayment(self, payment):
        pass