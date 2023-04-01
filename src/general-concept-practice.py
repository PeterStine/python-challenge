import random

"""
Functions inside module 'csv'

Output of dir(csv) = 
['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
"""
import csv

# Create a file to be read in later.
with open('python-challenge/src/file.csv', mode='w') as file:
    file.writelines("Test line")

# Open the file created in read-only mode
with open('python-challenge/src/file.csv', mode='r') as file:
    print(file.readline())

# Finding measures of central tendency on arrays
numberedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 80]
max(numberedList)
min(numberedList)
