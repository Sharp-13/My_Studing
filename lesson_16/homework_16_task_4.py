# Task 4
#
# Custom exception
#
# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`. Tips:
# Use __init__ method to extend functionality for saving messages to file
#
# ```

import datetime

class CustomException(Exception):
   def __init__(self, msg):
       self.msg = msg
       super().__init__(self.msg)
       with open('log.txt', 'a') as f:
           f.write(f'{datetime.datetime.now()} was raised CustomException with message "{self.msg}"\n')


raise CustomException('Some another error')