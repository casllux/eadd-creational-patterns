from payment.payment_abstract import PaymentGateway

class Esewa(PaymentGateway):
    """This class will have the necessary properties and methods to 
        process the payment through Esewa account. """

    def processPayment(self):
        return "Esewas payment method"
    

class Khalti(PaymentGateway):
    """This class will have the necessary properties and methods to 
        process the payment through Khalti account. """

    def processPayment(self):
        return "Khalti payment method"
    
    
class Paypal(PaymentGateway):
    """This class will have the necessary properties and methods to 
        process the payment through a Paypal account. """
    
    def processPayment(self):
        return "Paypal payment method"