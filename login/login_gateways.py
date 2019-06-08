from login.login_abstract import LoginGateway


class GoogleLogin(LoginGateway):
    """This class will have the necessary properties and methods to 
        process the login through a Google account. """

    def processLogin(self):
        return "Google Login method"


class FacebookLogin(LoginGateway):
    """This class will have the necessary properties and methods to 
        process the login through a Facebook account. """

    def processLogin(self):
        return "Facebook Login method"


class EmailLogin(LoginGateway):
    """This class will have the necessary properties and methods to 
        process the login through an email address. """
        
    def processLogin(self):
        return "Email Login method"