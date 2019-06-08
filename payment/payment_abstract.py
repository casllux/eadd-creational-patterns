from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    """This is an interface that the sub classes will inherit from,
    to implement the payment methods for the payment gateways defined. """


    def __init__(self):
        super().__init__()


    @abstractmethod
    def processPayment(self):
        pass