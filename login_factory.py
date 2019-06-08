from login.login_gateways import GoogleLogin, FacebookLogin, EmailLogin


class LoginFactory():
    """ This class contains the method that returns the objects of the login gateways defined.
        This allows for dynamic object creation by providing an interface for calling the 
        required objects as required. """

    @staticmethod
    def getLogin(login):
        """ This method returns the object of the login gateways specified in its argument parameter.
            This allows for dynamically creating objects of the login gateways as required by the user."""
            
        if login == 'google':
            return GoogleLogin()
        
        elif login == 'facebook':
            return FacebookLogin()

        elif login == 'email':
            return EmailLogin()

        return None
    