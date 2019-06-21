class MetaSingleton(type):
    """ This is the singleton class which will serve as the singleton metaclass
        so that other classes can also created as singleton classes.

         Metaclass is the 'class factory' in Python used to create objects which 
         are classes. Since, in Python everthing is an object including class
         so the class that creates class objects is metaclass.
         'type' is the built-in metaclass Python uses and we can also define our
          own metaclasses. """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """ The __call__ function is called whenever the object of the class is called.
            This modified __call__ function ensures that the class can have only a 
            single instance and if an instance of the class already exists it returns it.

            Defining a custom __call__() method in the meta-class allows the class instances
            to be called as a function
        """

        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

