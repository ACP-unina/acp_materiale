# calculator.py

### CASO CON __init__.py VUOTO NON funzionano i seguenti, bisogna aggiungere a __init__.py la variable __all__ = ['divider', 'multiplier']

import operations
from operations import * 

# from operations import multiplier, divider

# OPPURE
#

# dir() will return all the properties and methods, even built-in properties which are default for all object.
print("dir(operations): ", dir(operations))

# __file__ 
print("operations.__file__", operations.__file__)

mymultiplier = multiplier.Multiplier()
result = mymultiplier.multiply(2, 5)
print(f"2 x 5 is {result}")

mydivider = divider.Divider()
result = mydivider.divide(10, 2)
print(f"10 / 2 is {result}")

