from payment.payment_gateways import Esewa, Khalti, Paypal

class PaymentFactory():
    """ This class contains the method that returns the objects of the payment gateways defined.
        This allows for dynamic object creation by providing an interface for calling the 
        objects as required. """

    @staticmethod
    def getPayment(payment):
        """ This method returns the object of the payment gateways specified in its argument parameter.
            This allows for dynamically creating objects of the payment gateways as specified by the user."""
            
        if payment == 'esewa':
            return Esewa()
        
        elif payment == 'khalti':
            return Khalti()

        elif payment == 'paypal':
            return Paypal()

        return None
    