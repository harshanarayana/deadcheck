'''
Created on Dec 4, 2013

@author: harsnara
'''

class ArgumentMissingError(Exception):
    
    def __init__(self, message, argName):
        self.__argName = argName
        self.__message = message

    def get_arg_name(self):
        return self.__argName


    def get_message(self):
        return self.__message


    def set_arg_name(self, value):
        self.__argName = value


    def set_message(self, value):
        self.__message = value

    def __str__(self, *args, **kwargs):
        return repr(self.message)
    
    arg = property(get_arg_name, set_arg_name, "Missing Argument in the Input")
    message = property(get_message, set_message, "Error Message to display")