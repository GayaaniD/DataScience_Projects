import sys 
"""
The sys module in python provides various functions and variables that are
used to manipulate different parts of the python runtime environment. It allows operating 
on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter

So any exception that is basically getting control, the sys library automatically have that information
"""
from src.logger import logging

'''
whenever an expception get raised,push this on the custom message 
'''
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    '''
    this ecx_tb will give all the information like :
    --> on which file the exception occured
    --> on which line number exception has occured
    '''
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):#Constructor
        super().__init__(error_message)#inherit the init function from Exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    '''
    So whenever we raise the custom exception, first of all it will inherit the parent exception,
    whatever error message is basically coming from the particular function --> error_message_detail, will come over here
    and will initialize it to the calss variable or custom exception variable that is error message and the error details is basically tracked by sys
    '''
    def __str__(self):
        '''
        inherit this another functionality, so whenever we try to print it , it will getting all the error message here
        '''
        return self.error_message
    
    '''
    So in summary:
    --> Created function error_message_detail : give message how our message should look like inside our file w.r.t our custom exception
    --> Created own custom exception class which is inheriting from Exception & overritten the init method & create error message variable which will be populated from the already created function
    --> when we raise the custom exception in short when we print , it is going to print the error message itself
    '''

    '''
    It will be common for the entire code, so whenever we use try-catch and whenever inside the
    catch block we just raise custiom exception, this kind of formatted message will be coming that error 
    occured in python script name , line number and all other informations
    '''

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
    
# python exception.py --> error created and trigger logger file
            
