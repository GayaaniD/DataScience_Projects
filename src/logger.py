import logging
'''
Logger is for the purpose that any execution that probably happens, 
we should be able to log all those informations, execution in some files, so that we will be 
able to track of there is some errors even the custom exception error, try to log that into text file
'''
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#getcwd--> get current working directory
os.makedirs(logs_path,exist_ok=True)# exist_ok=True --> eventhough there is a file or folder, keep on appending the files inside that whenever we want to create the file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
'''
format --> timestamp,line number,name, level name, message --> this is how the entire message will get printed
'''

'''
Whenever get an exception, take that logging into logger file and use logging.info to put if inside the file 
'''

if __name__=='__main__':
    logging.info("Logging has started") 
    '''
    insidesrc folder , a new folder created as Log and inside that log foler, 
    there is a file created --> 04_06_2024_19_37_45.log --> with content --> [ 2024-04-06 19:37:45,242 ] 30 root - INFO - Logging has started
    '''

# python logger.py