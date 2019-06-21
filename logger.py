from singleton import MetaSingleton
import datetime
import os

class Logger(metaclass=MetaSingleton):
    """This Logger class is a implemented as a Singleton using the metaclass method.
        Here, the object of Logger can be used to log information and error into separate
        files. """

    _directory = 'Logs'
   
    def __init__(self):
        """ Used to initialze the objects of the class
            When object is initialized it checks if the directory specified
            exists or not, if not then creates it. """
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    # @classmethod
    # def config(cls,name):
    #     cls._filelog = name
    #     with open(cls._filelog, mode ='w') as log:
    #         log.write('Log created at '+ str(datetime.datetime.now()) + '\n')

    
    def info(self,log_str):
        """ This function is used to log informational messages into a separate
            log file specified. """
        with open('Logs/info.log', mode ='a') as log:
            log.write("\n<" + str(datetime.datetime.now()) + ">   INFO:: '"+ log_str + "'\n")

    
    def error(self, log_str):
        """ This function is used to log error messages into a separate
            log file specified. """
        with open('Logs/error.log', mode = 'a') as log:
            log.write("<" + str(datetime.datetime.now()) + ">   ERROR:: '" + log_str + "'\n")
