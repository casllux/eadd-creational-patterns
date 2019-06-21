from factory_producer import FactoryProducer
from logger import Logger


def payment():
    """ This method allows to access the payment gateways, with the object creation being 
        handled by two different classes: one for creating 'Payment' type object and 
        other for creating the 'specified payment gateway' object."""

    Factory = FactoryProducer.getFactory('payment')

    logger1 = Logger()
    logger1.info('Inside the payment method...')

    payment_method = str(input("Enter the payment gateway(Esewa, Khalti, Paypal): ")).lower()

    try:
        payment = Factory.getPayment(payment_method)
        print(payment.processPayment())
    except(AttributeError):
        logger1.error('Payment error...')
        print("No such payment portal!")


def login():
    """ This method allows to access the login gateways, with the object creation being 
        handled by two different classes: one for creating 'login' type object and 
        other for creating the 'specified login gateway' object."""

    Factory = FactoryProducer.getFactory('login')
           
    logger2 = Logger()
    logger2.info('Inside the login method...')
    
    login_method = str(input("Enter the login gateway(Google, Facebook, Email): ")).lower()

    try:
        login = Factory.getLogin(login_method)
        print(login.processLogin())
    except(AttributeError):
        logger2.error('Login error...')
        print("No such login portal!")


def main():
    """ The method is used to test the program and see if it works using the patterns."""
    
    # login_method = str(input("Enter the login gateway: ")).lower()

    # try:
    #     login = LoginFactory.getLogin(login_method)
    #     print(login.processLogin())
    # except(AttributeError):
    #     print("No such login portal!")

    logger = Logger()
    logger.info('Beginning of main...')

    waiting = True
    while waiting:
        print("\n1. Payment")
        print("2. Login")
        print("3. Exit")

        choice = str(input("?> "))

        if choice == '1':
           payment()

        elif choice == '2':
            login()

        elif choice == '3':
            waiting = False
        
        else:
            print('No such choice!')

    print("Finished...")
    logger.info('End of main...')



if __name__ == '__main__':
    main()