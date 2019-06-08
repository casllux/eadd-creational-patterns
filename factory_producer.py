from login_factory import LoginFactory
from payment_factory import PaymentFactory

class FactoryProducer():
    """This class allows to create objects of the individual 'Factory' classes, allowing further abstraction on the object calls of the 
        classes defined in the 'Factory' classes. """

    @staticmethod
    def getFactory(factory):
        if factory == 'payment':
            return PaymentFactory()

        elif factory == 'login':
            return LoginFactory()
        
        return None