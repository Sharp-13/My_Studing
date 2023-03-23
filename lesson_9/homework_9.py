# Task 1
#
# Imports practice
#
#  Make a directory with 2 modules; make a function in one of them;
#  then import this function in the other module and use that in your script of choice.



# Task 2
#
# The sys module.
#
#  The “sys.path” list is initialized from the PYTHONPATH environment variable.
#  Is it possible to change it from within Python? If so, does it affect where
#  Python looks for module files? Run some interactive tests to find it out.

import sys

print(sys.path)

sys.path.append('C:\\google-python-exercises\\basic\\solution')

print(sys.path)

from list1 import sort_last

unsorted_list = [(2, 3), (6, 3, 4), (1, 9,3,7), (2, 5)]
sorted_list = sort_last(unsorted_list)
print(sorted_list)

# Task 3
#
# Basics, import, work with os module
#
# Write a program that counts lines and characters in a file (similar to `wc` Unix-utility,
# for additional info about it follow the link:
# https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS or
# Linux - just call manual for this utility via command: `man wc`).
#
# Create a Python module called `mymod.py`, which has three functions:
#
# count_lines(name) function that reads an input file and counts the number of
#     lines in it (hint: file.readlines() does most of the work for you, and `len` does the rest)
# count_chars(name) function that reads an input file and counts the number of
#     characters in it (hint: file.read() returns a single string)
# test(name) function that calls both counting functions with a given input file­name.
#     Such a filename generally might be passed-in, hard-coded, input with raw_input,
#     or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
#
# All three `mymod.py` functions should expect a filename string to be passed in.
#
# Test your module interactively, using import and name qualification to fetch your exports.
#
# Does your PYTHONPATH need to include the directory where you created mymod.py?
#
# Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice;
# if you’re feeling ambitious, you may be able to improve this by passing an open file object
# into the two count functions (hint: file.seek(0) is a file rewind).