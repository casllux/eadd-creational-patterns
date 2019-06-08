# Python on its own doesn't provide abstract class. It comes with 'abc' module that provides the basis for defining Abstract Base Classes
# This modules also provides the decorators for defining a class method as abstract method.
from abc import ABC, abstractmethod

class LoginGateway(ABC):
    """This is an interface that the sub classes will inherit from,
        to implement the login methods for the login gateways defined. """

    
    def __init__(self):
        super().__init__()

    @abstractmethod
    def processLogin(self):
        pass