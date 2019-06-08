from login_factory import LoginFactory


def main():
    """ The method is used to test the program and see if it works using the patterns."""
    
    login_method = str(input("Enter the login gateway: ")).lower()

    try:
        login = LoginFactory.getLogin(login_method)
        print(login.processLogin())
    except(AttributeError):
        print("No such login portal!")

if __name__ == '__main__':
    main()