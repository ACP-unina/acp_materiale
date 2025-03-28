# calculator.py

### CASO senza __init__.py non funzionano i seguenti
#from operations import *

#import operations

## funziona solo il seguente
from operations import multiplier, divider

mymultiplier = multiplier.Multiplier()
result = mymultiplier.multiply(2, 5)
print(f"2 x 5 is {result}")

mydivider = divider.Divider()
result = mydivider.divide(10, 2)
print(f"10 / 2 is {result}")

