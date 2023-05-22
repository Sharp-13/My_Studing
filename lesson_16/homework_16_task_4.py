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
#    def __init__(self, msg):
#        try:
#            return CustomException(msg)
#        except CustomException:
#            with open('logs.txt', 'a') as f:
#                f.write(f'{datetime.now()} - CustomException was raised with message ({msg})')
    pass

raise CustomException('Some error')